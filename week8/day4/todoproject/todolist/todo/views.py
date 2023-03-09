from django.shortcuts import render
from .models import Todo, Category
from . import forms

# Create your views here.
# Create some views
# todo view : a form where the user can add a new task in the todo table.

#    title = models.CharField(max_length=255)
#     details = models.TextField()
#     has_been_done = models.BooleanField(default=False)
#     date_creation = models.DateTimeField(auto_now_add=True)
#     deadline_date = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey(Category)


def todo_add(request):
    # if the form is valid, save the form and redirect to the display_todos view

    form = forms.TodoForm(request.POST)
    if form.is_valid():
        print("form is valid")
        instance = form.save(commit=False)
        instance.save()
    else:
        print("form is not valid errors: ", form.errors)
    context = {
        "form": form,
    }
    return render(request, "newtodo.html", context)


def todo_delete(request, id):
    Todo.objects.filter(id=id).delete()
    return render(request, "todolist.html")


def complete_todo(request):
    todo_id = request.POST.get("todo_id")
    # call matching function using todo_id
    todo = Todo.objects.get(id=todo_id)
    todo.has_been_done = True
    todo.save()
    return render(request, "todolist.html")


# display_todos : where all the todos are displayed. For each todo, you need to display:
# the title, the details,
# the date_creation, the deadline_date,
# the category of the todo,
# a button “DONE” (see Exercise XP Gold)


# Hint : while creating the ‘add todo’ form, check how to add choice field to choose between categories
# Look here for Choice Field
# Look here for Multiple Choice Field
def todolist(request):
    todos = Todo.objects.all()
    return render(request, "todolist.html", {"todos": todos})


def index(request):
    return render(request, "index.html")
