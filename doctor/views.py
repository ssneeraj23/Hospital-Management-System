from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from .forms import *
from .models import *
import datetime

today = datetime.date.today()

# Create your views here.
# @login_required
def doctor(request):
    template = loader.get_template('doctor.html')
    return HttpResponse(template.render())
def pl(request):
    template = loader.get_template('patientList.html')
    return HttpResponse(template.render())
def pi(request):
    template = loader.get_template('patientInfo.html')
    return HttpResponse(template.render())
def ri(request):
    template = loader.get_template('resultInsert.html')
    return HttpResponse(template.render())
def pr(request):
    f = patientRegForm()
    context = {}
    context["form"]=f 
    return render(request,"patientReg.html",context)