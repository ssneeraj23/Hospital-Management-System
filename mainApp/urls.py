from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('main/', views.doctor_page, name='doctor_page'),
]