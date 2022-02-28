from django.db import models

# Create your models here.
class todo(models.Model):
    TaskName=models.CharField(max_length=90)
    TaskTime=models.CharField(max_length=30)
    CompletionStatus=models.BooleanField(default=False)
