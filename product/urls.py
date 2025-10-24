from django.urls import path
from product.views import *

app_name = "product"
 
urlpatterns = [
    path("index/",index),
    path("list_tasks/" , list_task , name="home"),
    path("change_task/<int:id_task>/" , change_done),
    path("create_task/" ,create_task , name="create_task"),
]