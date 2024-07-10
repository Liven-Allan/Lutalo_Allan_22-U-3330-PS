from django.db import models
from django.utils import timezone


# Create your models here.
class SoilMositure(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    Soil_level = models.FloatField()

    def __str__(self) :
        return  f"{self.timestamp} - {self.Soil_level}"
