from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from .forms import *

urlpatterns = [

    path('', LoginView.as_view(template_name='login.html',
         next_page='doctor', authentication_form=LoginForm), name='login'),
    path('doctorDash', views.docDashView, name='doctorDash'),
    path('patientList', views.patientListView, name='patientList'),
    path('patientInfo', views.patientInfoView, name='patientInfo'),
    path('logout', views.logout_view, name='logout'),
    path('access-denied', views.access_denied, name='access-denied')  # TODO
]
