
from django.urls import path,include
from .import views

urlpatterns=[

    path('availability',views.availabity,name ='availablity'),
    path('stock',views.stock,name='stock'),


]

