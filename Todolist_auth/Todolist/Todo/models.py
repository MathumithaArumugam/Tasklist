from django.db import models

# Create your models here.
class Users(models.Model):
    UserName=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)


class todo(models.Model):
    TaskName=models.CharField(max_length=90)
    TaskTime=models.CharField(max_length=30)
    CompletionStatus=models.BooleanField(default=False)
    UserId=models.IntegerField(default=1)