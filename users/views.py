from .models import User
from .serializers import UserSerializer, UserUpdateSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login


class UserList(APIView):
    def get(self, request):
        print(request.user)
        print(request.session.keys())

        users = User.objects.all()
        return Response(
            UserListSerializer(users, many=True).data, status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.filter(email=request.data["email"])
        if len(user):
            return Response({"message": "This email already registered!"})

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)

    def get(self, request, pk):
        print(request.session["current_user_id"])
        user = self.get_object(pk=pk)
        login(request, user)
        print(request.session.items())
        print(type(request.user))

        serializer = UserListSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = UserUpdateSerializer(user, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = self.get_object(pk=pk)
        user.delete()
        return Response({"msg": "User deleted"}, status=status.HTTP_202_ACCEPTED)
