from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length=64)
    description = models.TextField()
    date = models.DateField()
    # user = models.ForeignKey(User)