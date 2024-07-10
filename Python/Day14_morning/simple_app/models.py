from django.db import models
from django.utils import timezone

# Step 1

# Create your models here.
class SoilMoistureReading(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    moisture_level = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - {self.moisture_level}"