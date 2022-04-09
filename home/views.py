from django.shortcuts import render
from django.views import generic
def show_home(request):
    return render(request,'blog/home.html')


def show_profile(request):
    return render(request,'blog/profile.html')
