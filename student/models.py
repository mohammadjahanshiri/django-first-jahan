from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    fullname = models.CharField(max_length=128)
    score = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="user_student" , unique=True)
    def __str__(self):
        return self.fullname
    
class Teachers(models.Model):
    fullname = models.CharField(max_length=128)
    score = models.PositiveIntegerField(default=0)
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="user_teacher" , unique=True)
    def __str__(self):
        return self.fullname
    

class Course(models.Model):
    title = models.CharField(max_length=128)
    code = models.PositiveIntegerField()
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    students = models.ManyToManyField(Students , related_name="courses")
    def __str__(self):
        return self.title

    
class Profile(models.Model):
    bio = models.TextField()
    avatar = models.CharField(max_length=128 , blank=True)
    phone_number = models.CharField(max_length=15 ,blank=True)
    img = models.CharField(blank=True)
    file = models.CharField(blank=True)
    student = models.OneToOneField(Students ,on_delete=models.CASCADE ,related_name="profile_student" , blank=True)
    teacher = models.OneToOneField(Teachers , on_delete=models.CASCADE ,related_name="profile_teacher" , blank=True)
    def __str__(self):
        return self.bio