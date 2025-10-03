from django.shortcuts import render
from django.http import HttpResponse
from product.models import Task

def index(request):
    list_tasks = Task.objects.filter(done=True)
    titles = []
    for i in list_tasks:
         titles.append(i.title)
    return HttpResponse(title1(titles))


def title1(objs_list):
    titles = []
    for i in objs_list:
        titles.append(len(i))
    return (str(titles))