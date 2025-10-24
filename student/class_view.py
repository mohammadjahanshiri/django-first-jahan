from django.views import View
from student.models import *
from student.forms import StudentForm
from django.shortcuts import render , redirect


class AllStudents(View):
    html_file = "student/all_student.html"

    def get(self , request):
        form = StudentForm()
        all_students = Students.objects.all()
        context = {"students": all_students ,
                   "form" : form}
        return render(request , self.html_file , context)