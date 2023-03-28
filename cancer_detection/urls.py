from django.urls import path
from . import views

urlpatterns = [
    path('detect/', views.cancerDetection, name='detect'),
]