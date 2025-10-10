from django.shortcuts import render
from student.models import Students


def student_view(request):
    create1 = Students.objects.create(fullname="mohammad" , username="mohammad" , score=16)
    all_students = Students.objects.filter(score__gt=15)
    context = {"students": all_students ,
               "student_add" : create1}
    html_file = "student/all_student.html"
    return render (request , html_file , context)

def add_student(request):
    create1 = Students.objects.create(fullname="mohammad" , username="mohammad" , score=16)
    context = {"student_add" : create1}
    html_fil = "student/all_student.html"
    return render (request , html_fil , context)