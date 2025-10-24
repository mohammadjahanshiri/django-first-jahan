from django.shortcuts import render
from django.http import HttpResponse
from product.models import Task
from product.forms import TaskForm


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
    task = Task.objects.get(id=id_task)
    task.done = not task.done
    task.save()
    task2 = Task.objects.filter(id=id_task)
    context = {"task" : task ,
               "task2" : task2}
    html_file = "product/change_task.html"
    return render(request , html_file , context)

def create_task(request):
    form = TaskForm(request.POST)
    html_file = "product/create_task.html"
    all_task = Task.objects.all()
    if request.method == "GET":
        context = {"students" : all_task ,
                   "form" : form}
        return render(request , html_file , context)
    elif request.method == "POST":
        title1 =request.POST.get("title")
        category1 = request.POST.get("category")
        description1 = request.POST.get("description")
        date1 = request.POST.get("date")
        student1 = request.POST.get("student")
        Task.objects.create(title=title1 , category=category1 , description=description1 , date=date1 , student_id=student1 )
        context1 = {"form" : form}
        return render(request , html_file , context1)


