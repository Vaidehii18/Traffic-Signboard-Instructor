from django.db import models

# Create your models here.
class service(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.models.IntegerField()