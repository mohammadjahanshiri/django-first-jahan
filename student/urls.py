from django.urls import path
from student.views import *

urlpatterns = [
    path("add/",add_student),
    path("view_student/",student_view),
    path("task_student/<int:st_id>/",task_student),
    path("all_courses/" ,courses_view),
    path("course_students/" , course_students),
    path("student_courses/", student_courses),
]