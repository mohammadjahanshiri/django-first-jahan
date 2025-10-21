from django.urls import path
from product.views import *
 
urlpatterns = [
    path("index/",index),
    path("list_tasks/" , list_task),
    path("change_task/<int:task_id>/" , change_done),
]