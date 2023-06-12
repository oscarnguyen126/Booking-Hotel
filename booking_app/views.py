from .models import RoomFacility, RoomInfo
from .serializers import RoomSerializer, FacilitySerializer
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser

# TODO: double check mutative fn
#   [] validate registered fields
#   [] omit unregistered fields


class RoomList(generics.ListCreateAPIView):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save()
            facilities = RoomFacility.objects.filter(
                name__in=request.data["facilities"]
            )
            for facility in facilities:
                room.facilities.add(facility)
            room.save()
        return Response(serializer.data)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomSerializer

    def put(self, request, *args, **kwargs):
        room = RoomInfo.objects.get(pk=kwargs["pk"])
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid(raise_exception=True):
            room = serializer.save()
            facilities = RoomFacility.objects.filter(
                name__in=request.data["facilities"]
            )
            room.facilities.clear()
            for facility in facilities:
                room.facilities.add(facility)
            room.save()
            return Response(serializer.data)


class FacilityList(generics.ListCreateAPIView):
    queryset = RoomFacility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomFacility.objects.all()
    serializer_class = FacilitySerializer
