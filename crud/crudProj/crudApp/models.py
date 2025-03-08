from django.db import models

class Student(models.Model):
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    email = models.EmailField(unique=True)
    dateOfBirth = models.DateField(null=True)
    course = models.CharField(max_length=100)
    enrollmentDate = models.DateField()