from django.urls import path
from product.views import index
 
urlpatterns = [
    path("index/",index)
]