# Create your views here.
from .models import *
from django.shortcuts import render
from django.contrib import messages
import datetime
from django.http import HttpResponse


def index(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name','')
        city = request.POST.get('city','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        time = request.POST.get('ptime','')
        date = datetime.datetime.now()
        # print(name,city,phone,email,time,date)
        contact = Contact(name=name,email=email,time=time,phone=phone,city=city,date=date)
        contact.save()
    return render(request,'bt/index.html')

def about(request):
    return render(request,'bt/about.html')

def dashboard(request):
    return render(request,'bt/dashboard.html')

def listing(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        property = request.POST.get('property','')
        message = request.POST.get('message', '')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        date= datetime.datetime.now()
        # print(name,phone,email,message,property,date)
        Inquiry = inquiry(name=name,message=message,email=email,phone=phone,property=property,date=date)
        Inquiry.save()
        messages.success(request,"Message Sent. We will right back to you.")
    return render(request,'bt/listing.html')

def listings(request):
    return render(request,'bt/listings.html')

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        authenticate = Register
        credentail = authenticate.objects.filter(username=username,password=password).count()
        if credentail >0:
           user = Register.objects.filter(username=username)
           name1 =  [item.fname for item in user]
           punctuation = '''['']'''
           name = ""
           for char in name1:
               if char not in punctuation:
                   name = name + char
           print(name)
           messages.success(request,"login successfully.")
           files = {'name':name}
           return render(request, 'bt/dashboard.html',files)
        else:
            messages.warning(request,"username or password is incorrect. Please login again ")
            return render(request, 'bt/login.html')
    return render(request,'bt/login.html')
    # return HttpResponse("hello")

def register(request):
    if request.method=="POST":
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname', '')
        username = request.POST.get('username','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        date = datetime.datetime.now()
        # print(fname,lname,phone,email,username,password,date)
        register = Register(fname=fname,lname=lname,email=email,password=password,phone=phone,username=username,date=date)
        register.save()
        messages.info(request,"Registration done successfully. Please login.")
        return render(request, 'bt/register.html')
    return render(request,'bt/register.html')

def search(request):
    return render(request,'bt/search.html')