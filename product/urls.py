from django.urls import path
from product.views import index,list_task
 
urlpatterns = [
    path("index/",index),
    path("list_tasks/" , list_task)
]