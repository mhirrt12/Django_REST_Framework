from django.contrib import admin

# Register your models here.
from .models import Student,Book, Product

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    search_fields = ('name', 'email')
    list_filter = ('age',)
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    # search_fields = ('title',)
    # list_filter = ('price',)