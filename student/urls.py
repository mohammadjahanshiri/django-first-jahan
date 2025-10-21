from django.urls import path
from student.views import *

urlpatterns = [
    path("add/",add_student),
    path("view_student/",student_view),
    path("task_student/<int:st_id>/",task_student),
    path("all_courses/" ,courses_view),
    path("course_students/" , course_students),
    path("student_courses/", student_courses),
    path("student_scores/<int:scor_e>/" , student_score),
    path("courses_detail/<int:cours_e>/" , course_url_view),
    path("student_courses_id/<int:id_stu>/" , student_courses_id)
]