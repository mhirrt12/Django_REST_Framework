from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("students/<int:id>", views.students),
    
    path("form/",views.add_book),
]