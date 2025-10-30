from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.views import View
from account.forms import UserRegisterForm , LoginForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages


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
                return redirect("account:user_login")
        return render(request , self.html_file , {"form" : self.form , "message" : "username or password wrong or repeat before."})


class LoginView(View):

    form = LoginForm()
    html_file = "account/user_login.html"
    def get(self , request):
        return render(request , self.html_file , {"form" : self.form})
    
    def post(self , request):
        user = authenticate(request , username=request.POST["username"] , password=request.POST["password"])
        if user is not None and user.is_authenticated:
            login(request , user)
            return redirect("student:create_student")
        return render(request , self.html_file , {"form" : self.form , "message" : "password or username is wrong."})
    
class logoutView(View):
    def get(self , request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("account:user_login")

class DeleteAccountView(View):
    def get(self , request , *args , **kwargs):
        user = request.user
        logout(request)
        user.delete()
        request.session.flush()
        return redirect("student:student_list")

        
            
