from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.utils import timezone

def take_form(request):
  print("In here")
  if request.method=="POST":
    print("Got there--------------------------")
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    template = loader.get_template('result.html')
    context = {
       "fname":fname,
       "lname":lname,
    }
    print(request.POST)
    return HttpResponse(render(request,"result.html",context))  
  else :
     fname="Neeraj"
     lname="Boddeda"
     template = loader.get_template('result.html')
     context = {
       "fname":fname,
       "lname":lname,
     }
     return HttpResponse(render(request,"result.html",context))  
  
def put_form(request):
    template = loader.get_template('form.html')
    print("Residing in main-----------------------")
    return render(request,"form.html")

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




