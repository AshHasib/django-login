from django.shortcuts import render
from .forms import LoginForm, SignupForm
from .models import Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def index(request):

    return render(request, 'index.html', {})


def login(request):
    form = LoginForm()

    if request.method =='POST':
        form = LoginForm(request.POST)

        if(form.is_valid()):
            data = form.cleaned_data

            username = data['username']
            password = data['password']

            
    return render(request, 'login.html', {'form':form})


def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():

            paswd = form.cleaned_data['password']
            repasswd = form.cleaned_data['re_password']

            if paswd == repasswd:
                profile = Profile()
                data = form.cleaned_data
                profile.name = data['name']
                profile.email = data['email']
                profile.phoneNumber = data['phoneNumber']
                profile.profile_pic = data['profile_pic']
                profile.password = data['password']
                profile.save()

                return redirect('login')

            else:
                return HttpResponse('Passwords do not match. Try again')


    return render(request, 'signup.html', {'form':form})

def explore(request):

    return render(request, 'explore.html', {})


def aboutUs(request):

    return render(request, 'about.html', {})

def signUpSuccess(request):
    return render(request, 'signup_success.html', {})