from django.db import models


class RoomInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    roomsize = models.IntegerField(default=30)
    price = models.FloatField()
    facilities = models.ManyToManyField('RoomFacility', blank=True)
    img = models.TextField()

    def __str__(self):
        return self.name


class RoomFacility(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name