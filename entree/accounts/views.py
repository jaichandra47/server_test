from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from accounts.models import Registration
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('login_home')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')


    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=='POST':
        print("***** Printed")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        phone = request.POST['phone']
        year = request.POST['year']
        college = request.POST['college']
        branch = request.POST['branch']
        print(first_name,last_name,user_name,email,phone,year,college,branch)
        outcome = Registration(first_name = first_name,last_name=last_name,user_name=user_name,email=email,phone=phone,year=year,college=college,branch=branch)
        outcome.save()
    return render(request, 'register.html')


