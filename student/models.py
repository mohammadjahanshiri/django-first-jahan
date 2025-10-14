from django.db import models


class Students(models.Model):
    fullname = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    score = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.fullname
    

class Course(models.Model):
    title = models.CharField(max_length=128)
    code = models.PositiveIntegerField()
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    students = models.ManyToManyField(Students)
    def __str__(self):
        return self.title