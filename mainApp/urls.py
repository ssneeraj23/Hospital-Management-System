from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from .forms import *

urlpatterns = [

    path('', LoginView.as_view(template_name='login2.html', next_page='doctor', authentication_form=LoginForm), name='login'),
    path('doctor',views.doctor, name = 'doctor'),
    path('pl',views.pl, name = 'pl'),
    path('pi',views.pi, name = 'pi'),
    path('ri',views.ri, name = 'ri'),
    path('logout', views.logout_view, name = 'logout'),
    path('password_reset', views.password_reset, name = 'password_reset'), # TODO
]