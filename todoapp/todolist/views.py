from django.shortcuts import render, redirect
from .models import TodoList, Category
from django.shortcuts import get_object_or_404


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager
    if request.method == "POST": 
        if "taskAdd" in request.POST: 
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            status = request.POST["status_select"]
            Todo = TodoList(title=title, content=content, due_date=date,
            category=Category.objects.get(name=category), status=status)
            Todo.save()  # saving the todo
            return redirect("/%5E$")  # reloading the page

        if "taskupdate" in request.POST:
            checkedlist = request.POST["checkedbox"]
            todo = TodoList.objects.get(pk=checkedlist)
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            status = request.POST["status_select"]
            todo = TodoList(id=checkedlist, title=title, content=content, due_date=date,
                            category=Category.objects.get(name=category), status=status)
            todo.save()  # saving the todo
            return redirect("/%5E$")  # reloading the page

        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"]
            todo = TodoList.objects.get(pk=checkedlist)
            todo.delete()
            return redirect("/%5E$")
        
        if "addcategory" in request.POST:
            name=request.POST["inputcategory"]
            category=Category(name=name)
            category.save() 
            return redirect("/%5E$")

    return render(request, "index.html", {"todos": todos, "categories":categories})
