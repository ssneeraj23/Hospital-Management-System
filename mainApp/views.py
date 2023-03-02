from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

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
