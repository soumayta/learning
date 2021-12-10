from django.db import models

# Create your models here.
class product(models.Model):
    pro_id = models.IntegerField()
    pro_name = models.CharField(max_length=25)
    pro_type = models.CharField(max_length=25)
