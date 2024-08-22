from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your models here.
class CustomUser(AbstractUser):
    USER = (
        ('1', "HOD"),
        ('2', "Teacher"),
        ('3', "Student")
    )

    user_type = models.CharField(choices=USER, max_length=100, default=1)
    profile_pic = models.ImageField(upload_to="media/profile_pic")
    password = models.CharField(max_length=20, null=True)


class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    number = models.IntegerField(null=True)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #password = models.CharField(max_length=20, null=True)
    number = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=100)
    #course_id = models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

   

    
