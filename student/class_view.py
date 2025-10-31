from django.views import View
from student.models import *
from student.forms import StudentForm , CreateStudentForm , CreateCourseForm , CreateProfileForm
from django.shortcuts import render , redirect
from django.db import IntegrityError


class AllStudents(View):
    html_file = "student/all_student.html"

    def get(self , request):
        form = StudentForm()
        all_students = Students.objects.all()
        context = {"students": all_students ,
                   "form" : form}
        return render(request , self.html_file , context)
    

class CreateStudentView(View):

    html_file = "student/createstudent.html"
    form = CreateStudentForm()

    def get(self , request):
        return render(request , self.html_file , {"form" : self.form})
    

    
    def post(self, request):
        st_form = CreateStudentForm(request.POST)
        if st_form.is_valid():
            try: 
                st_form.save()
            except IntegrityError:
                st_form.add_error('username' , "This username is already exists")
            # new_student = Students.objects.create(
                # fullname=request.POST["fullname"],
                # username="username",
                # phone_number=request.POST["phone_number"]
            # )
            if st_form:
                return redirect("student:student_list")
        return render(request , self.html_file , {"form" : self.form , "message" : "username or password wrong or repeat before."})
    


class AllCoursesView(View):
    html_file = "student/all_courses2.html"
    course1 = Course.objects.all()
    form = CreateCourseForm()

    def get(self , request):
        return render(request , self.html_file , {"form" :self.form , "all_courses" : self.course1})
    
    def post(self , request):
        cou_form = CreateCourseForm(request.POST)
        if cou_form.is_valid():
            cou_form.save()
            # new_course = Course.objects.create(
            #     title=request.POST["title"],
            #     code=request.POST["code"],
            #     description=request.POST["description"],
            #     start_date=request.POST{"start_date"},
            #     end_date=request.POST["end_date"],
            #     students=request.POST["students"],
            # )
            if cou_form:
                return redirect("student:all_courses")
        
        return render(request , self.html_file , {"form" :self.form , "all_courses" : self.course1})


class CreateProfileView(View):
    html_file = "student/create_profile.html"
    form = CreateProfileForm()
    def get(self , request):
        return render(request , self.html_file , {"form" :self.form})
    
    def post(self,request):
        prof_form = CreateProfileForm(request.POST)
        if prof_form.is_valid():
            new_prof = Profile.objects.create(
                bio=request.POST["bio"],
                avatar=request.POST["avatar"],
                student_id=request.POST["student"]
            )
            if new_prof:
                return redirect("student:allstudent")
        return render(request , self.html_file , {"form" :self.form})
    
class AllTeachersView(View):
    html_file = "student/allteachers.html"
    all_teachers = Teachers.objects.all()
    def get(self , request):
        return render(request , self.html_file ,{"teachers" : self.all_teachers})