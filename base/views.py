from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)
