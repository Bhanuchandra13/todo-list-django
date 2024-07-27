from django.shortcuts import render, redirect,get_object_or_404
from todolist_app.models import TaskList
from todolist_app.forms import Taskform
from django.contrib import messages
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required


@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            # form.save(commit=False).manager=request.user
            # form.save()
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            messages.success(request, "New Task Added!")
            return redirect('todolist')
    else:
        form = Taskform()
        
    all_tasks = TaskList.objects.filter(manager = request.user)
    paginator = Paginator(all_tasks,5)    #Objects and no. of objects to be in a page is that number 5
    page = request.GET.get('pg')
    all_tasks = paginator.get_page(page)
    return render(request, 'todolist.html', {'all_tasks': all_tasks, 'form': form})

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager ==request.user:
        task.delete()
    else:
        messages.error(request,"Access restricted, You are not allowed")
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(TaskList, pk=task_id)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('todolist')
    else:
        form = Taskform(instance=task)

    return render(request, 'edit.html', {'task_obj': task, 'form': form})

@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager ==request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,"Access restricted, You are not allowed")  
    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')


def index(request):
    return render(request, 'index.html', {'welcome_text': "Welcome to the home page"})

@login_required
def about(request):
    return render(request, 'about.html', {'welcome_text': "Welcome to the About page"})

@login_required
def contact(request):
    return render(request, 'contact.html', {'welcome_text': "Welcome to the contact page"})
