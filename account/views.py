from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.views import View
from account.forms import UserRegisterForm


class RegisterView(View):

    form = UserRegisterForm()
    html_file = "account/register.html"
    def get(self , request):
        return render(request , self.html_file , {"form" : self.form})


    def post(self, request):
        st_form = UserRegisterForm(request.POST)
        if st_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST["username"],
                email="",
                password=request.POST["password"]
            )
            if new_user:
                return redirect("student:student_list")
        return render(request , self.html_file , {"form" : self.form , "message" : "username or password wrong or repeat before."})
