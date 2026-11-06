from django.shortcuts import render

from core import models

# Create your views here.

def home(request):
    return render(request,"home.html")

def cart(request):
    return render(request,"cart.html")

def order(request):
    return render(request,"order.html")

def todo(request):
    if request.method == "POST":
        req=request.POST.get("task")
        task = models.todo(task=req)
        task.save()
    mytodo = models.todo.objects.all()
    data = {'todos':mytodo}
    return render(request,"todo.html",data)

def deleteTodo(request):
    if request.method=="GET":
        todoId = int(request.GET.get("id"))
        models.todo.objects.filter(id=todoId).delete()
    return todo(request)

