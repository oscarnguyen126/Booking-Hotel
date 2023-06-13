from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import bcrypt
from django.shortcuts import get_object_or_404


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(
            UserSerializer(users, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.filter(email=request.data["email"])
        if len(user):
            return Response({"message": "This email already registered!"})

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            salt = bcrypt.gensalt()
            serializer.password = bcrypt.hashpw(
                request.data["password"].encode("utf-8"), salt
            )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserDetailSerializer(user, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response({"msg": "User deleted"}, status=status.HTTP_202_ACCEPTED)
