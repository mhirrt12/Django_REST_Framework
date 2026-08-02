from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django!")
def students(request,id):
    return HttpResponse(f"Student ID: {id}")
def profile (request,username):
    return HttpResponse(f"welcome {username} to your profile page")