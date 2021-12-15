from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('check/', views.check, name='check'),
    path('', views.index, name='index'),
]