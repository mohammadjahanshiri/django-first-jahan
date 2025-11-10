from django.views import View
from student.models import *
from student.forms import *
from django.shortcuts import render , redirect , get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin


class AllStudentsView(View):
    html_file = "student/all_student.html"

    def get(self , request):
        all_students = Students.objects.all()
        context = {"students": all_students}
        return render(request , self.html_file , context)
    
class AllTeachersView(View):
    html_file = "student/allteachers.html"
    all_teachers = Teachers.objects.all()
    def get(self , request):
        return render(request , self.html_file ,{"teachers" : self.all_teachers})
    

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
    def get(self , request , pk):
        html_file = "student/all_courses.html"
        courses = get_object_or_404(Course , pk=pk)
        return render(request , html_file , {"courses" : courses})


class CreateCoursesView(LoginRequiredMixin , View):
    login_url = 'account:user_login'
    html_file = "student/all_courses21.html"
    course1 = Course.objects.all()
    form = CreateCourseForm()

    def get(self , request):
        return render(request , self.html_file , {"form" :self.form , "all_courses1" : self.course1})
    
    def post(self , request):
        cou_form = CreateCourseForm(request.POST)
        if cou_form.is_valid():
            cou_form.save()
            if cou_form:
                return redirect("student:create_student")
        
        return render(request , self.html_file , {"form" :self.form , "all_courses" : self.course1})
    
# class EnrollCoursesView(View):
#     html_file = "student/enrollcourse.html"
#     form = EnrollCourseForm()
#     courses1 = Course.objects.all()
#     def get(self , request):
#         return render (request , self.html_file , {"courses" : self.courses1 , "form" :self.form })
    
#     def post(self , request):
#         enroll_form = EnrollCourseForm(request.POST)
#         if not request.user.profile.student or not request.user.is_authenticated:
#             return redirect("student:create_student")
#         elif enroll_form.is_valid():
#             enroll_form.save()
#             return redirect("student:all_courses")
#         return render(request , self.html_file , {"form" :self.form , "all_courses" : self.course1})



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
    
class EnrollCoursesView(LoginRequiredMixin , View):
    login_url = 'account:user_login'
    
    def get(self , request):
        html_file = "student/all_courses2.html"
        all_courses = Course.objects.all()
        return render (request , html_file , {"courses" : all_courses})
    def post(self , request ):
        student = request.user.user_profile.profile_student
        select_ids = request.POST.getlist('courses')
        for course_id in select_ids:
            course = Course.objects.get(id=course_id)
            course.students.add(student)
        return redirect("student:allstudent")
    