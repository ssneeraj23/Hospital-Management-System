from django.db.models import F
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from .forms import *
from .models import *
from datetime import datetime

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('userRedirect')
    else:
        return redirect('login')


@login_required
def userRedirect(request):
    userProf = request.user.profile
    if userProf.role == 'd':
        return redirect('doctorDash')
    elif userProf.role == 'fdo':
        return redirect('frontDesk')
    elif userProf.role == 'deo':
        return redirect('dataEntry')
    else:
        return redirect('access-denied')


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
        context = {"doctor": doctorObj,
                   "appointments": app_list, 'form': PatientInfoForm()}
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
        appReportForm = FileAppointmentReportForm()
        testReportForm = UploadTestReportForm()
        opReportForm = UploadOperationReportForm()
        if 'test_submit' in request.POST:
            testReportForm = UploadTestReportForm(request.POST, request.FILES)
            if testReportForm.is_valid():
                testReportForm.save()
        elif 'operation_submit' in request.POST:
            opReportForm = UploadOperationReportForm(
                request.POST, request.FILES)
            if opReportForm.is_valid():
                opReportForm.save()
        elif 'appointment_submit' in request.POST:
            appReportForm = FileAppointmentReportForm(
                request.POST, request.FILES)
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
        patientRegForm = PatientRegForm(request.POST, request.FILES)
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
        admissionRegForm = AdmissionForm(request.POST, request.FILES)
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
        scheduleTestForm = ScheduleTestForm(request.POST, request.FILES)
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
        scheduleOperationForm = ScheduleOperationForm(
            request.POST, request.FILES)
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
        makeAppointmentForm = MakeAppointmentForm(request.POST, request.FILES)
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
        dischargeForm = DischargeForm(request.POST, request.FILES)
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
        form = PatientInfoForm(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            data = form.cleaned_data
            patient = Patient.objects.get(pk=data['patientID'].pk)
            context['patient'] = patient
            context['appointments'] = Appointment.objects.filter(patientID=patient.pk)
            context['tests'] = Test.objects.filter(patientID=patient.pk)
            context['operations'] = Operation.objects.filter(patientID=patient.pk)
        else:
            messages.error(request, "Invalid input")
        return render(request, 'patientInfo.html', context)


@login_required
def patientListView(request):
    if request.user.profile.role != 'd':
        return redirect('access-denied')
    elif request.method == 'GET':
        docObj = request.user.profile.doctor
        operations = docObj.doctors.all()
        apps = docObj.doctor_assigned.all()
        context = {'operations': operations, 'appointments' : apps}
        return render(request, 'patientList.html', context)

@login_required
def fileDownloadView(request):
    path = request.POST.get('fileName')
    print(path)
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def logout_view(request):
    logout(request)
    return redirect('login')


def access_denied(request):
    return render(request, 'access_denied.html')
