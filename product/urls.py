from django.urls import path
from product.views import *

app_name = "product"
 
urlpatterns = [
    path("index/",index),
    path("list_tasks/" , list_task , name="home"),
    path("change_task/<int:task_id>/" , change_done),
]