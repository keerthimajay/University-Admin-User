from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
   course_name=models.CharField(max_length=255)
   fee=models.CharField(max_length=255)

class StudentDetails(models.Model):
   course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
   student_fname=models.CharField(max_length=255)
   student_lname=models.CharField(max_length=255)
   age=models.IntegerField()
   address=models.CharField(max_length=255)
   doj=models.DateField()

class TeacherDetails(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=125)
    img = models.ImageField(upload_to='image/',null=True)
    address = models.CharField(max_length=125)
    doj = models.DateField()
