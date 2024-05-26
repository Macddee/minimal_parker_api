from django.urls import path
from . import views

urlpatterns = [
    path('process-parking/', views.ProcessParking.as_view(), name='login'),
]