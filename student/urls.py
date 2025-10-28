from django.urls import path
from student.views import *
from student.class_view import AllStudents , CreateStudentView , AllCoursesView , CreateProfileView

app_name = "student"

urlpatterns = [
    path("add/",add_student),
    path("view_student/",student_view , name="student_list"),
    path("task_student/<int:st_id>/",task_student),
    path("all_courses/" ,courses_view , name="all_courses"),
    path("course_students/" , course_students),
    path("student_courses/", student_courses),
    path("student_scores/<int:scor_e>/" , student_score),
    path("courses_detail/<int:cours_e>/" , course_url_view),
    path("student_courses_id/<int:id_stu>/" , student_courses_id),
    path("all_student1/" , AllStudents.as_view() , name="allstudent"),
    path("create_student/" , CreateStudentView.as_view() , name="create_student" ),
    path("create_course/" , AllCoursesView.as_view() , name="create_course"),
    path("create_profile/" , CreateProfileView.as_view() , name="create_profile")
]