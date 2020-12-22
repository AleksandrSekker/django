from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        print(request.POST )
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == 'DELETE':
        post = TodoListItem.objects.delete()
    context = {'post':post,'form': form}
    return render(request, 'home.html', context)

    

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            print(request.POST )
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You successfully registred')
                return redirect('login')
            
    context = {'form':form}
    return render(request, 'registration.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            send_mail(
                    'Login',
                    f'User {username} login in site',
                    settings.EMAIL_HOST_USER,
                    ['sekkerpleksandr@gmail.com',],
                    fail_silently=False,
                        )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'You type wrong login or password, please try again')
    context = {}
    return render(request, 'login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def contactMe(request):
    
    context = {}
    return render(request, 'contact.html', context)