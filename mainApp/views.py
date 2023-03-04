from django.db.models import F
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# from .forms import *
from .models import *
import datetime

today = datetime.date.today()

# Create your views here.
# @login_required

def doctor(request):
    # request.user contains the user object 
    try:
        doc = get_object_or_404(Doctor, doctor__username=request.user.get_username()) # returns the doctor object with the given username
    except:
        return HttpResponse('Error 404')
    else:
        return render(request, 'doctor.html', {'doctor': doc}) # pass the doctor as context to the template

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