from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world")


def pages(request):
    return render(request , 'first.html')


def polls(request):
    #return HttpResponse('My name is polls')
    return render(request,'first.html')
