from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm, TodoUpdateForm

def todos(request):
    todo = Todo.objects.all()
    return render(request, 'core/index.html', {
        'todo': todo
    })

def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()

    return render(request, 'core/create_todo.html', {
        'form':form
    })

def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoUpdateForm(request.POST or None, instance=todo)
    if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoUpdateForm()

    return render(request, 'core/update_todo.html', {
        'form':form,
        'todo': todo
    })

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect('/')
    return render(request, 'core/delete_confirm.html', {
        'todo': todo
    })