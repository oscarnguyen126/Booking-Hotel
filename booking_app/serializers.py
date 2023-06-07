from rest_framework import serializers
from .models import RoomFacility, RoomInfo


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFacility
        fields = ('id', 'name',)


class RoomSerializer(serializers.ModelSerializer):
    facilities = FacilitySerializer(many=True, read_only=True)

    class Meta:
        model = RoomInfo
        fields = ['id','name', 'description', 'price', 'img', 'facilities', 'roomsize']

        def create(self, validated_data):
          return RoomInfo.objects.create(**validated_data)


# option 1:
# rewrite server to be able to handle content-type = multipart/form-data

# option 2:
# keep using file as a string to keep content-type = application/json

#  client or server? to convert base64 image back to binary?