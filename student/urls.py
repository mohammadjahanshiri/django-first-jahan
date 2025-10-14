from django.urls import path
from student.views import add_student , student_view , task_student , courses_view

urlpatterns = [
    path("add/",add_student),
    path("view_student/",student_view),
    path("task_student/",task_student),
    path("all_courses/" ,courses_view)
]