from django.db import models
from django.contrib.auth.models import User 
from student.models import Students

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    student = models.ForeignKey(Students , on_delete=models.CASCADE)
    # user = models.ForeignKey(User)
    def __str__(self):
        return self.title
    

class TypeCategory(models.Model):
    title = models.CharField(max_length=256)
    tasks = models.ManyToManyField(Task)
    def __str__(self):
        return self.title