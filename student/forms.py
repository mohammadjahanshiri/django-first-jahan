from django.forms import ModelForm
from student.models import Students

class StudentForm(ModelForm):

    class Meta:
        model = Students
        fields = ["fullname" , "username" , "phone_number"] 