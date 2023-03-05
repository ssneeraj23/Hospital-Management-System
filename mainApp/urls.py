from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from .forms import *

urlpatterns = [

    path('', LoginView.as_view(template_name='login.html', next_page='doctor', authentication_form=LoginForm), name='login'),
    path('base', views.base, name='base'),
    path('dataEntry/', views.dataEntry, name='dataEntry'),
    path('frontDesk/', views.frontDesk, name='frontDesk'),
    path('doctor/', views.doctor, name='doctor'),
    # path('doctor',views.doctor, name = 'doctor'),
    path('patientReg/', views.patientReg, name='patientReg'),
    path('patientList',views.patientList, name = 'patientList'),
    path('patientInfo/',views.patientInfo, name = 'patientInfo'),
    # path('ri',views.ri, name = 'ri'),
    path('logout', views.logout_view, name = 'logout'),
    # path('password_reset', views.password_reset, name = 'password_reset'), # TODO
    # path('access-denied', views.access_denied, name='access-denied') # TODO
]
