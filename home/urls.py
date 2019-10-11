from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/',views.login, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('signup/success/', views.signUpSuccess, name = 'signupsuccess'),
    path('explore/',views.explore, name = 'explore'),
    path('about/',views.aboutUs, name = 'about'),
]