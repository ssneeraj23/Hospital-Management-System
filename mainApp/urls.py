from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from . import views
from .forms import *

urlpatterns = [
    path('', views.home, name='home'),
    path('login', LoginView.as_view(template_name='login.html',
         next_page='userRedirect', authentication_form=LoginForm), name='login'),
    path('userRedirect', views.userRedirect, name='userRedirect'),
    path('doctorDash', views.docDashView, name='doctorDash'),
    path('patientList', views.patientListView, name='patientList'),
    path('patientInfo', views.patientInfoView, name='patientInfo'),
    path('frontDesk', views.frontDeskOpDashView, name='frontDesk'),
    path('dataEntry', views.dataEntryOpDashView, name='dataEntry'),
    path('patientReg', views.patientRegView, name='patientReg'),
    path('admissionReg', views.admissionRegView, name='admissionReg'),
    path('scheduleTest', views.scheduleTestView, name='scheduleTest'),
    path('scheduleOperation', views.scheduleOperationView, name='scheduleOperation'),
    path('makeAppointment', views.makeAppointmentView, name='makeAppointment'),
    path('discharge', views.dischargeView, name='discharge'),
    path('filedownload', views.fileDownloadView, name='filedownload'),
    path('logout', views.logout_view, name='logout'),
    path('access-denied', views.access_denied, name='access-denied')
]
