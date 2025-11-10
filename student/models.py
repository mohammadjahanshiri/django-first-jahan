from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    fullname = models.CharField(max_length=128)
    score = models.PositiveIntegerField(default=0)
    profile = models.OneToOneField("Profile" , on_delete=models.CASCADE , related_name="profile_student" , blank=True , null=True)
    def __str__(self):
        return self.fullname
    
class Teachers(models.Model):
    fullname = models.CharField(max_length=128)
    score = models.PositiveIntegerField(default=0)
    profile = models.OneToOneField("Profile" , on_delete=models.CASCADE , related_name="profile_teacher" , blank=True ,null=True)
    def __str__(self):
        return self.fullname
    

class Course(models.Model):
    title = models.CharField(max_length=128)
    code = models.PositiveIntegerField(blank=True , null=True)
    description = models.TextField(blank=True , null=True)
    start_date = models.DateTimeField(blank=True , null=True)
    end_date = models.DateTimeField(blank=True , null=True)
    is_available = models.BooleanField(default=True)
    students = models.ManyToManyField(Students , related_name="courses_student" , blank=True , null=True)
    teacher = models.ForeignKey(Teachers , on_delete=models.CASCADE , related_name="courses_teacher" ,  blank=True , null=True)
    def __str__(self):
        return self.title
    
# class EnrollmentCourse(models.Model):
#     courses = models.ManyToManyField(Course  , name="courses" ,  blank=True , null=True )
#     students = models.ManyToManyField(Students  , related_name="enrollmentcourses" ,blank=True , null=True)
#     date_enrolled = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.students.fullname} : {self.courses.title}"

    
class Profile(models.Model):
    bio = models.TextField()
    avatar = models.CharField(max_length=128 , blank=True)
    phone_number = models.CharField(max_length=15 ,blank=True)
    img = models.CharField(blank=True)
    file = models.CharField(blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="user_profile" , blank=True ,null=True)
    is_student = models.BooleanField(default=True)
    def __str__(self):
        return self.bio