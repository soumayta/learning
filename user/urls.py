from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
    path('a',views.index,name = 'index'),
    path('first',views.pages,name = 'first'),
    path('polls',views.polls , name='polls'),
]

