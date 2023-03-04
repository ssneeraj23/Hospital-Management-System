from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('doctorView',views.doctor, name = 'doctor'),
    path('patientList',views.pl,name = 'pl'),
    path('patientInfo',views.pi,name = 'pi'),
    path('resultInsert',views.ri,name = 'ri')
]