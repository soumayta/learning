from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def availabity(request):
    return HttpResponse('The product is available') 

def stock(request):
    return render(request , 'first.html')

