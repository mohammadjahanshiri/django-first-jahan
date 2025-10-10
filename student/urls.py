from django.urls import path
from student.views import add_student , student_view

urlpatterns = [
    path("add/",add_student),
    path("view_student/",student_view)
]