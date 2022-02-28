from django.db import models

# Create your models here.
class student(models.Model):
    StudentName=models.CharField(max_length=90)
    RollNumber=models.CharField(max_length=90)
    Grade=models.CharField(max_length=90)
    PhoneNumber=models.IntegerField(max_length=10)
    FatherName=models.CharField(max_length=90)
    MotherName=models.CharField(max_length=90)
    Address=models.CharField(max_length=150)
    