from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse   
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models  import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    #title='hello world'
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                 return render(request, 'signup.html', {
                   'form': UserCreationForm(),
                   'error':'Usuario ya existe'
                 })
        
        return render(request, 'signup.html', {
          'form': UserCreationForm(),
           'error':'Passwor no coincide'
        })
@login_required
def tasks(request):
    tasks=Task.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'tasks.html',{'tasks':tasks})   

@login_required
def tasks_complete(request):
    tasks=Task.objects.filter(user=request.user,datecompleted__isnull=False).order_by
    ('-datecompleted')
    return render(request,'tasks.html',{'tasks':tasks})   
@login_required
def create_tasks(request):
    if request.method=='GET':
        return render(request,'create_tasks.html',{
          'form':TaskForm
        })
    else:
         try:
             form=TaskForm(request.POST)
         #print(form)
             new_tasks= form.save(commit=False)
             new_tasks.user= request.user   
             new_tasks.save()
             return redirect('tasks')
         except ValueError:
             return render(request,'create_tasks',{
                 'form':TaskForm,
                 'error': 'Por favor introduce una tarea valida '
             })

@login_required
def tasks_deta(request, tasks_id):
    if request.method=='GET':
        task= get_object_or_404(Task,pk=tasks_id, user=request.user)
        form=TaskForm(instance=task)
        return render(request,'tasks_dete.html',{
           'task':task, 
            'form':form
          }) 
    else:
        try:
            task= get_object_or_404(Task,pk=tasks_id, user=request.user)
            form=TaskForm(request.POST,instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'tasks_dete.html',{
                'task':task,
                'form':form,
                'error':'Tarea no actualzizada'
                
            })

@login_required
def complete_taks(request, task_id):
   if request.method=='POST':  
     task = get_object_or_404(Task, pk=task_id, user=request.user) 
     task.datecompleted = timezone.now()
     task.save()
     return redirect('tasks')
@login_required
def  delete(request, task_id):
    if request.method=='POST':
     task = get_object_or_404(Task, pk=task_id, user=request.user) 
     task.datecompleted = timezone.now()
     task.delete()
     return redirect('tasks')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    
    if request.method=='GET':
        return render(request,'signing.html',{
        'form':AuthenticationForm
        })
    else:
        
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signing.html',{
                'form':AuthenticationForm,
                'error':'Usuario incorrecto'
            })
        else:
            login(request,user)
            return redirect('tasks',)
        

  