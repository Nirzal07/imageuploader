from django.shortcuts import render, redirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ImageForm, RegisterUser
from .models import Images

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user:
            login(request, user)
            return redirect(home)
        else:
            messages = "Didn't find such account"
            context = {'message': messages}
    context = {}
    return render(request, 'imageapp/login.html', context)

@login_required
def home(request):
    user_images = Images.objects.filter(user= request.user).order_by('-upload_time')
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user_form= form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect(home)
    else:
        form = ImageForm()
    context = {'form': form, 'user_images': user_images}
    return render(request, 'imageapp/home.html', context)

def register(request):
    if request.method != 'POST':
        form= RegisterUser()
    else:
        form= RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'imageapp/register.html', context)

