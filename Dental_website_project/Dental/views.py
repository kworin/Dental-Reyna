from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Dental/Dental.html')

# views.py
from django.shortcuts import render, redirect
import time

