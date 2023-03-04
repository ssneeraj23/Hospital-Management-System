from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doctorView',views.doctor, name = 'doctor'),
    path('patientList',views.pl,name = 'pl'),
    path('patientInfo',views.pi,name = 'pi'),
    path('resultInsert',views.ri,name = 'ri')
]