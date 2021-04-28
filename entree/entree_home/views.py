from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import Query

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_home(request):
    return render(request, 'login_home.html')

def services(request):
    return render(request, 'services.html')

def about_us(request):
    return render(request, 'about_us.html') #It takes 3 arguments

def contact_us(request):
    return render(request, 'services.html') #It takes 3 arguments

def get_in_touch(request):
    if request.method=='POST':
        print("***** Printed")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name,email,phone,message)
        qry = Query(name=name,email=email,phone=phone,message=message)
        qry.save()
    return redirect('/')