from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import *

@receiver(post_save , sender=Students)
def CreateStudentSignal(sender , instance , created , **kwargs):

    if created:
        Profile.objects.create(
            bio = f"{instance.fullname}'s  bio",
            student = instance
        )

@receiver(post_save , sender=Teachers)
def CreateTeachersSignal(sender , instance , created , **kwargs):

    if created:
        Profile.objects.create(
            bio = f"{instance.fullname}'s bio" , 
            teachers = instance
        )