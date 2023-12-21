from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required


def login_page(request):
    return render(request, 'accounts/login.html')
def register_page(request):
    return render(request, 'accounts/register.html')