from django.db.models import F
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# from .forms import *
from .models import *
from datetime import datetime

# Create your views here.

@login_required
def doctor(request):
    # request.user contains the user object 
    try:
        doc = get_object_or_404(Doctor, username__username=request.user.get_username()) # returns the doctor object with the given username
    except:
        return HttpResponse('Error 404')
    else:
        current_datetime = datetime.now()
        # app_list = get_list_or_404(Appointment, doctorID=doc.pk) & get_list_or_404(Appointment, endTime__gt=current_datetime) # TODO: add patient names
        app_list = Appointment.objects.filter(doctorID=doc.pk, endTime__gt=current_datetime)
        # app_list = []
        context = {"doctor": doc, "appointments": app_list}
        return render(request, 'doctor.html', context) # pass the doctor as context to the template

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