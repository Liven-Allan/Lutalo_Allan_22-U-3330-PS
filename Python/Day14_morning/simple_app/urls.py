from django.urls import path
from .views import moisture_list

# Step 4

urlpatterns = [
    path('', moisture_list, name='mositure_list' ),
    
]