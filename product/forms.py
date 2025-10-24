from django import forms
from student.models import Students

class TaskForm(forms.Form):
    title = forms.CharField()
    category = forms.CharField(max_length=256)
    description = forms.CharField()
    date = forms.DateField()
    student = forms.ModelChoiceField(queryset=Students.objects.all())