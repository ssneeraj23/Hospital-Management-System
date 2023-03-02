from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    return HttpResponse("<h1>Welcome to this ugly website.</h1><br>Have a <a href=\"https://www.youtube.com/watch?v=izGwDsrQ1eQ\">rickroll</a>.")