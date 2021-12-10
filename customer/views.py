from django.shortcuts import render
from django.http import HttpResponse,response
# Create your views here.

def name(request):
    return HttpResponse('<h2>  Name of the customer <h2>')

def choice(request):
    return render(request ,'first.html')

def option(request):
    return render(request,'second.html')
