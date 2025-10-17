from django.contrib import admin
from student.models import Students
from student.models import Course
from student.models import Profile

admin.site.register(Students)
admin.site.register(Course)
admin.site.register(Profile)