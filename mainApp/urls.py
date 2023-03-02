from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('main/', views.take_form, name='take_form'),
    path('', views.put_form, name='put_form'),
]