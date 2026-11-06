from django.shortcuts import render

from core import models

# Create your views here.

def home(request):
    products = models.product.objects.all()
    return render(request,"home.html",{'products':products})

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

def product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        imageUrl=request.POST.get("imageUrl")
        product=models.product(name=name,price=price,desc=desc,imageUrl=imageUrl)
        product.save()
    return render(request,"products.html")
