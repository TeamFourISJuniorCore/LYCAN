from django.db import models

# Create your models here.
class Student (models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    funfact = models.CharField(max_length=255, blank=True)
    sectionNum = models.IntegerField()
    groupNum = models.IntegerField()
    gender = models.CharField(max_length=1)
    photoUrl = models.CharField(max_length=500)
    feedback = models.CharField(max_length=300, blank=True)
