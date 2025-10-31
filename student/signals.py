from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Students , Profile

@receiver(post_save , sender=Students)
def CreateStudentSignal(sender , instance , created , **kwargs):

    if created:
        Profile.objects.create(
            bio = f"{instance.fullname}'s  bio",
            student = instance
        )