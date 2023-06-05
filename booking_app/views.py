from .models import RoomFacility, RoomInfo
from .serializers import RoomSerializer, FacilitySerializer
from rest_framework import generics
from rest_framework.response import Response


class RoomList(generics.ListCreateAPIView):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomSerializer
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomInfo.objects.all()
    serializer_class = RoomSerializer


class FacilityList(generics.ListCreateAPIView):
    queryset = RoomFacility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomFacility.objects.all()
    serializer_class = FacilitySerializer
