from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock_tracker, name='stock_tracker'),
]
