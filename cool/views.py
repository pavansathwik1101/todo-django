from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages



@login_required
def index(request):
    user = request.user
    print("user", user)
    tasks = Task.objects.filter(user=user)
    data={'user':user,'tasks':tasks}
    context = {'data': data}
    return render(request, 'index.html', context)

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('name')
        user = request.user
        cool=Task.objects.create(title=title, user=user)
        cool.save()
        return redirect('index')

    return render(request, 'index.html')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('index')
def cool(request):
    return render(request,'register.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user=User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('login')

            #return redirect('login')  # Redirect to the desired page after successful registration and login

    return render(request, 'register.html')

   
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')


    return render(request, 'login.html')
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

    
