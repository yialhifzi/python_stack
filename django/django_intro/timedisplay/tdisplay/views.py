from email.utils import localtime
from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def root(request):
    return redirect("/time_display")

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", localtime())
    }
    return render(request,'index.html', context)
# Create your views here.
