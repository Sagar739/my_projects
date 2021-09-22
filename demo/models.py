from django.db import models

# Create your models here.

class Person(models.Model):
    first_name=models.CharField(max_length=75)
    last_name=models.CharField(max_length=75)
    email=models.CharField(max_length=150)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    city=models.CharField(max_length=50)

    class Meta:
        db_table = 'Person'

    def __str__(self):
        return self.first_name + self.last_name

class Participant(models.Model):
   
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=150)

    class Meta:
        db_table = "participants"

class Student(models.Model):
    s_no =  models.CharField(max_length=50)
    s_name = models.CharField(max_length=100)
    s_percentage = models.FloatField()

    # class Meta:
    #     db_table = 'student'

    def __str__(self):
       return f"{self.s_no} {self.s_name} {self.s_percentage}"