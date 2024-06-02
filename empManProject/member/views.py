from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def loginUser(req):
    if req.method == "POST":
        userName = req.POST['userName']
        password = req.POST['password']
        user = authenticate(req, username=userName, password=password)
        if user is not None:
            login(req,user)
            return redirect('index')
        else:
            messages.success(req,("Invalid Credentials, Try Again"))
            return redirect('login')
    else:
        return render(req,'login.html', {})