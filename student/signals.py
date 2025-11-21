from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import *

# @receiver(post_save , sender=Students)
# def CreateStudentSignal(sender , instance , created , **kwargs):

#     if created:
#         Profile.objects.create(
#             bio = f"{instance.fullname}'s  bio",
#             student = instance
#         )

# @receiver(post_save , sender=Teachers)
# def CreateTeachersSignal(sender , instance , created , **kwargs):

#     if created:
#         Profile.objects.create(
#             bio = f"{instance.fullname}'s bio" , 
#             teachers = instance
#         )

@receiver(post_save , sender=User)
def CreateStudentSignal(sender , instance , created , **kwargs):

    if created:
        if instance.is_student:
            Students.objects.creat(
                fullname= f"{instance.user.first_name} {instance.user.last_name}" , 
                profile= instance
            )
        else:
            Teachers.objects.create(
                fullname= f"{instance.user.first_name} {instance.user.last_name}" ,
                profile= instance
            )