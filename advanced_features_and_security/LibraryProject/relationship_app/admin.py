from django.contrib import admin
#from django.urls import path, include
from .models import Book, Library

# Register your models here.
# urlpatterns = [

#     path('admin/', admin.site.urls),
    
# ]

admin.site.register(Book)
admin.site.register(Library)