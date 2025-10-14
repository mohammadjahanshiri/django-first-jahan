from django.shortcuts import render
from student.models import Students , Course
from product.models import Task


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

def task_student(request):
    task_student1 = Task.objects.filter(student_id=1)
    context = {"task_student1" : task_student1}
    html_fil = "student/student1.html"
    return render(request , html_fil , context)

def courses_view(request):
    course1 = Course.objects.all()
    context = {"all_courses" : course1}
    html_file = "student/all_courses.html"
    return render(request , html_file , context)