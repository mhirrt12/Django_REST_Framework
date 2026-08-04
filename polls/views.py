from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .forms import BookForm

def add_book(request):
    form = BookForm()

    return render(
        request,
        "book.html",
        {"form": form}
    )
def home(request):
    return render(request, "polls/home.html")
def students(request,id):
    return HttpResponse(f"Student ID: {id}")
def profile (request,username):
    return HttpResponse(f"welcome {username} to your profile page")