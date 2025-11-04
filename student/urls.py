from django.urls import path
from student.views import *
from student.class_view import *

app_name = "student"

urlpatterns = [
    path("view_student/",student_view , name="student_list"),
    path("task_student/<int:st_id>/",task_student),
    path("course_students/" , course_students),
    path("student_courses/", student_courses),
    path("student_scores/<int:scor_e>/" , student_score),
    path("courses_detail/<int:cours_e>/" , course_url_view),
    path("student_courses_id/<int:id_stu>/" , student_courses_id),
    path("all_student1/" , AllStudentsView.as_view() , name="allstudent"),
    path("create_student/" , CreateStudentView.as_view() , name="create_student" ),
    path("create_course/" , CreateCoursesView.as_view() , name="create_course"),
    path("create_profile/" , CreateProfileView.as_view() , name="create_profile"),
    path("all_teachers/" , AllTeachersView.as_view() , name="all_teachers"),
    path("all_courses/" , AllCoursesView.as_view() , name="all_courses"),
    path("enroll_course/" , EnrollCoursesView.as_view() , name="enroll_courses"),
]
