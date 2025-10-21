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

def task_student(request , st_id):
    task_student1 = Task.objects.filter(student_id=st_id)
    context = {"task_student1" : task_student1}
    html_fil = "student/student1.html"
    return render(request , html_fil , context)

def courses_view(request):
    course1 = Course.objects.all()
    context = {"all_courses" : course1}
    html_file = "student/all_courses.html"
    return render(request , html_file , context)

def student_courses(request):
    students = Course.objects.all()
    context = {"students" : students}
    html_file = "student/student_course.html"
    return render(request , html_file , context)

def course_students(request):
    course = Students.objects.all()
    context = {"courses" : course}
    html_file = "student/course_students.html"
    return render(request , html_file , context)

def student_score(request , scor_e):
    score_filter = Students.objects.filter(score__gt=scor_e)
    context = {"scores" : score_filter}
    html_file = "student/score_student.html"
    return render(request,html_file,context)

def course_url_view(request , cours_e):
    course_filter = Course.objects.filter(id=cours_e)
    context = {"coursess" : course_filter}
    html_file = "student/course_url_view.html"
    return render(request , html_file , context)

def student_courses_id(request , id_stu):
    students_id = Students.objects.filter(id=id_stu)
    context = {"student_courses" : students_id}
    html_file = "student/id_student.html"
    return render(request , html_file , context)