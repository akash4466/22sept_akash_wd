from django.db import models

# Create your models here.
class stud(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.DateField()
    mobil=models.BigIntegerField()
    address=models.TextField()
