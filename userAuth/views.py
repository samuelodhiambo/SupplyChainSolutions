from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import resolve
from .forms import CreateUserForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import UserProfile

# Create your views here.
def loginView(request, template='login.html'):
    if request.user.is_authenticated:
        return redirect('home')
    next = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next'):
                url = request.GET['next']
                url = str(url)
                if url == '/add/' or str(url) == '/add/':
                    return HttpResponseRedirect('/add/')
                if url == '/showCart/' or str(url) == 'showCart':
                    return HttpResponseRedirect('/showCart/')
            return redirect('home')
        error = 'Credentials do not match'
        return render(request, template, {'error': error})
    return render(request, template, {'next': next})

def registerView(request, template='signup.html'):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            profile = UserProfile()
            profile.user = request.user
            profile.phone = request.POST.get('phone')
            profile.user_type = request.POST.get('user_type')
            profile.save()
            return redirect('home')
        return render(request, template, {'form': form})
    form = CreateUserForm()
    return render(request, template, {'form': form})

def logoutView(request):
    logout(request)
    return redirect('home')

    