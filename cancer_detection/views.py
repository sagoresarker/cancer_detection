from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cancerDetection(request):
    return HttpResponse('This is cancer detection page!')