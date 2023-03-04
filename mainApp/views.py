from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from .forms import *
from django.utils import timezone

def doctor_page(request):
   doctor_name="Thomas Wayne"
   #assuming I know the doctorId after he logs in 
   doctorId=1
   current_time = timezone.now()
   appointments=Appointment.objects.filter(doctorID=doctorId, endTime__gte=current_time)
   patients = [Appointment.patientID.name for appointment in appointments]
   context={
      "patient_name":patients,
      "times" : appointments,
      "doc_name": doctor_name,
   }
   return render(request,"doctor.html",context)

def doctor_patient_info(request):
   #assuming I have the patient ID
   patientid=2
   specific_patient=Patient.objects.filter(id=patientid)
   name=specific_patient[0].name

   #reference  <img src="{{ patient.profile_picture.url }}" alt="{{ patient.name }} profile picture">
   all_appo_results=Appointment.objects.filter(patientID=patientid)
   op_repos=Operation.objects.filter(patientID=patientid)
   test_repos=Test.objects.filter(patientID=patientid)
   context={
      "app_results":all_appo_results,
      "op_results":op_repos,
      "test_results":test_repos
   }
   return render(request,"doctor.html",context)

def patients_treated(request):
   patients=Patient.objects.all()
   context={
      "patient":patients
   }
   return render(request,"patients_treated.html",context)
