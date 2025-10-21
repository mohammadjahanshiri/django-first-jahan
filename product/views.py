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


def list_task(request):
    list1 = Task.objects.all()
    # list3 = []
    # for text in list1:
    #     list3.append(text.title)

    list4 = {"task" : list1}
    return render(request , "product/new.html" , list4)

def change_done(request , id_task):
    task_id = Task.objects.filter(id=id_task)
    context = {"student_courses" : task_id}
    html_file = "product/change_task.html"
    return render(request , html_file , context)