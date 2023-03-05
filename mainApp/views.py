from django.db.models import F
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

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
        doctorObj = request.user.profile.doctor
        app_list = Appointment.objects.filter(
            doctorID=doctorObj, startTime__gt=current_datetime)
        context = {"doctor": doctorObj, "appointments": app_list, 'form' : PatientInfoForm()}
        # pass the doctor as context to the template
        return render(request, 'doctor.html', context)


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
            testReportForm = UploadTestReportForm(request.POST)
            if testReportForm.is_valid():
                testReportForm.save()
        elif 'operation_submit' in request.POST:
            opReportForm = UploadOperationReportForm(request.POST)
            if opReportForm.is_valid():
                opReportForm.save()
        elif 'appointment_submit' in request.POST:
            appReportForm = FileAppointmentReportForm(request.POST)
            if appReportForm.is_valid():
                appReportForm.save()
    context = {'appointment_form': appReportForm,
               'test_form': testReportForm, 'operation_form': opReportForm}
    return render(request, 'dataEntry.html', context)


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
    return render(request, 'patientReg.html', {'form': patientRegForm})


@login_required
def admissionRegView(request):
    # only front desk operator
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        admissionRegForm = AdmissionForm()
    elif request.method == 'POST':
        admissionRegForm = Admission(request.POST)
        if admissionRegForm.is_valid():
            admissionRegForm.save()
    return render(request, 'admissionReg.html', {'form': admissionRegForm})


@login_required
def scheduleTestView(request):
    # only front desk operator
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        scheduleTestForm = ScheduleTestForm()
    elif request.method == 'POST':
        scheduleTestForm = ScheduleTestForm(request.POST)
        if scheduleTestForm.is_valid():
            scheduleTestForm.save()
    return render(request, 'scheduleTest.html', {'form': scheduleTestForm})


@login_required
def scheduleOperationView(request):
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        scheduleOperationForm = ScheduleOperationForm()
    elif request.method == 'POST':
        scheduleOperationForm = ScheduleOperationForm(request.POST)
        if scheduleOperationForm.is_valid():
            scheduleOperationForm.save()
    return render(request, 'scheduleOperation.html', {'form': scheduleOperationForm})


@login_required
def makeAppointmentView(request):
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        makeAppointmentForm = MakeAppointmentForm()
    elif request.method == 'POST':
        makeAppointmentForm = MakeAppointmentForm(request.POST)
        if makeAppointmentForm.is_valid():
            makeAppointmentForm.save()
    return render(request, 'makeAppointment.html', {'form': makeAppointmentForm})


@login_required
def dischargeView(request):
    if request.user.profile.role != 'fdo':
        return redirect('access-denied')
    elif request.method == 'GET':
        dischargeForm = DischargeForm()
    elif request.method == 'POST':
        dischargeForm = DischargeForm(request.POST)
        if dischargeForm.is_valid():
            dischargeForm.save()
    return render(request, 'dischargeForm.html', {'form': dischargeForm})


@login_required
def patientInfoView(request):
    if request.user.profile.role != 'd':
        return redirect('access-denied')
    elif request.method == 'GET':
        return redirect('doctorDash')
    elif request.method == 'POST':
        form = PatientInfoForm(request.POST)
        context = {}
        if form.is_valid():
            patient = Patient.objects.filter(pk=form.patientID)
            context['patient'] = patient
        else:
            messages.error("Invalid input")
        return render(request, 'patientInfo.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
