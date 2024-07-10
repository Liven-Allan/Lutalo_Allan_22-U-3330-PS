from django.shortcuts import render
from .models import SoilMoistureReading
# step 3

# Create your views here.
def moisture_list(request):
    readings = SoilMoistureReading.objects.all().order_by('-timestamp')
    return render(request, 'simple_app/moisture_list.html', {'soil_readings':readings})

