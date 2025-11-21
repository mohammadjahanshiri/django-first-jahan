from rest_framework.views import APIView
from rest_framework.response import Response 
from student.models import *
from django.shortcuts import get_object_or_404
from rest_framework import status

class AllStudentsApi(APIView):
    def get(self , request):
        student_ids = Students.objects.all().values_list("fullname" , flat=True)
        students_dict = {"names" : student_ids}
        return Response(students_dict)
    
class StudentDetailApi(APIView):
    def get(self , request , pk):
        student_id = Students.objects.filter(pk=pk).values_list("fullname" , flat=True)
        student_id2 = Students.objects.filter(pk=pk).values_list("score" , flat=True)
        student_dict = {"fullname" : student_id
                        , "score" : student_id2}
        return Response(student_dict)
    
class AllCoursesApi(APIView):
    def get(self , request):
        courses_ids = Course.objects.all().values_list("title" , flat=True)
        courses_dict = {"title" : courses_ids}
        return Response(courses_dict)
    
class CoursesDetailApi(APIView):
    def get(self , request , pk):
        course_id = Course.objects.get(pk=pk)
        course_dict = {
            "title" : course_id.title , 
            "description" : course_id.description ,
        }
        return Response(course_dict)
    
class EnrollCorsesApi(APIView):
    # def get(self , request):
    #     courses_ids = Course.objects.all().values_list("title" , flat=True)
    #     courses_dict = {"title" : courses_ids}

    def post(self,request):
        student = request.user.user_profile.profile_student
        courses_id = request.data("course_id")
        if not courses_id:
            return Response({
                "error" : "course_id is not required"
            } , status=status.HTTP_400_BAD_REQUEST)
        try:
            course = Course.objects.get(id=courses_id)
        except Course.DoesNotExist:
            return Response({"error" : "course not found"} , status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if not user.is_authenticated:
            return Response({"error" : "authentication required"} , status=status.HTTP_401_UNAUTHORIZED)
        already = Course.objects.filter(students=user , id=course).exists()
        if already:
            return Response({"error" : "already enrolled"} , status=status.HTTP_400_BAD_REQUEST)
        course.students.add(student)
        course.save()
        return Response(request.user.id  ,status=status.HTTP_201_CREATED)
    
class ProfileApi(APIView):
    def get(self , request , pk):
        profile_id = Profile.objects.filter(pk=pk).values_list("bio" , flat=True)
        profile_number = Profile.objects.filter(pk=pk).values_list("phone_number" , flat=True)
        profile_dict = {"profile" : profile_id , "phone_number" : profile_number}
        return Response(profile_dict)
    