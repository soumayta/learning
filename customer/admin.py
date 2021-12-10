from django.contrib import admin
from .models import client, customer


# Register your models here.
admin.site.register(customer)
admin.site.register(client)
