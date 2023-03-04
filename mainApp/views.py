from django.db.models import F
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from .forms import *
from .models import *
from datetime import datetime

# Create your views here.

@login_required
def docDashView(request):
    if request.user.profile.role != 'd':
        return redirect('access-denied')
    # request.user contains the user object 
    else:
        current_datetime = datetime.now()
        doctorObj = request.user.doctor
        app_list = Appointment.objects.filter(doctorID=doctorObj, startTime__gt=current_datetime)
        context = {"doctor": doctorObj, "appointments": app_list}
        return render(request, 'doctor.html', context) # pass the doctor as context to the template

@login_required
def frontDeskOpDashView(request):
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    else:
        return render(request, 'frontDesk.html')

@login_required
def dataEntryOpDashView(request):
    if request.user.profile.role != 'deo':
        return redirect('access-denied')
    elif request.method == 'GET':
        appReportForm = FileAppointmentReportForm()
        testReportForm = UploadTestReportForm()
        opReportForm = UploadOperationReportForm()
    elif request.method == 'POST':
        if 'test_submit' in request.POST:
            pass
        elif 'operation_submit' in request.POST:
            pass
        elif 'appointment_submit' in request.POST:
            pass
    return render(request, 'dataEntry.html')

@login_required
def patientRegView(request):
    # only front desk operators can register new patients
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        patientRegForm = PatientRegForm()
    elif request.method == 'POST':
        patientRegForm = PatientRegForm(request.POST)
        if patientRegForm.is_valid():
            patientRegForm.save()
    return render(request, 'patientReg.html', {'form' : patientRegForm})

@login_required
# def 

def pl(request):
    template = loader.get_template('patientList.html')
    return HttpResponse(template.render())
def pi(request):
    template = loader.get_template('patientInfo.html')
    return HttpResponse(template.render())
def ri(request):
    template = loader.get_template('resultInsert.html')
    return HttpResponse(template.render())

def password_reset(request):
    return HttpResponse('<h1>Password reset page.</h1>') # TODO

def logout_view(request):
    logout(request)
    return redirect('login')