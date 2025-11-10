from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from student.models import *

@receiver(post_save , sender=User)
def CreateStudentSignal(sender , instance , created , **kwargs):

    if created:
        Profile.objects.create(
            bio = f"{instance.first_name}'s  bio",
            user=instance
        )