from django.forms import ModelForm
from student.models import *
from django.core.exceptions import ValidationError
from django import forms

class StudentForm(ModelForm):

    class Meta:
        model = Students
        fields = ["fullname" ] 

class CreateStudentForm(ModelForm):

    class Meta:
        model = Students
        fields = ["fullname" ]

        def clean_username(self):
            username = self.cleaned_data['username']
            if Students.objects.filter(username=username).exists():
                raise ValidationError("This username is already exists")
            return username
        
class CreateCourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ["title","code","description","start_date","end_date"]


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["bio" , "avatar" ]


# class EnrollCourseForm(forms.ModelForm):
#     class Meta:
#         model = EnrollmentCourse
#         fields = ["courses"]