from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loginUser(request):
    return HttpResponse("This is login page!.")

def registerUser(request):
    return HttpResponse("This is registration page!.")