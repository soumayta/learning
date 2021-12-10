from django.db import models
from products.models import product

# Create your models here.

class customer(models.Model):
    cus_id = models.IntegerField()
    cus_name = models.CharField(max_length=25)
    cus_review = models.CharField(max_length=45)

class client(models.Model):
    customer_a = models.ForeignKey('customer',null=True,blank=True,on_delete=models.SET_NULL)
    product_a = models.ForeignKey(product,null=True,blank=True,on_delete=models.SET_NULL)
    cli_address = models.CharField(max_length=40)
    cli_comment = models.CharField(max_length=40)
