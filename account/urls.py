from django.urls import path
from account.views import *

app_name = "account"
 
urlpatterns = [
    path("register/",RegisterView.as_view() , name="user_register"),
    path("login/",LoginView.as_view() , name="user_login"),
    path("logout/", logoutView.as_view() , name="user_logout"),
    path("delete_account/", DeleteAccountView.as_view() , name="user_delete_account"),
]