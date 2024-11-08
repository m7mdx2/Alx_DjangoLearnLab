from django.urls import path
from . import views

urlpatterns = [
    path('', views.unread_notifications, name='unread_notifications'),
]