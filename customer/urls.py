from django.urls import path
from .import views

urlpatterns=[
    path('name', views.name , name ='name'),
    path('choice', views.choice , name = 'choice'),
    path('option',views.option , name='option'),
]