from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from .forms import *

urlpatterns = [

    path('', LoginView.as_view(template_name='login.html',
         next_page='doctor', authentication_form=LoginForm), name='login'),
    path('doctorDash', views.docDashView, name='doctorDash'),
    path('patientList', views.pl, name='patientList'),
    path('patientInfo', views.pi, name='patientInfo'),
    path('ri', views.ri, name='ri'),
    path('logout', views.logout_view, name='logout'),
    path('password_reset', views.password_reset, name='password_reset'),  # TODO
    path('access-denied', views.access_denied, name='access-denied')  # TODO
]
