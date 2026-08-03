from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, "home.html")
def students(request,id):
    return HttpResponse(f"Student ID: {id}")
def profile (request,username):
    return HttpResponse(f"welcome {username} to your profile page")