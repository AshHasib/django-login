from django.shortcuts import render
from .forms import LoginForm, SignupForm
# Create your views here.

def index(request):

    return render(request, 'index.html', {})


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form':form})


def signup(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def explore(request):

    return render(request, 'explore.html', {})


def aboutUs(request):

    return render(request, 'about.html', {})