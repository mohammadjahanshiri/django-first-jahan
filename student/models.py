from django.db import models


class Students(models.Model):
    fullname = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    score = models.PositiveIntegerField()
    def __str__(self):
        return self.fullname