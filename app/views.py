from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse 
# Create your views here.

def insert_user(request):
    EUFO=UserForm()
    d={'EUFO':EUFO}

    if request.method=='POST':
        UFDO=UserForm(request.POST)
        if UFDO.is_valid():
            UFDO.save()
            return HttpResponse('insert_User is Done Succesfully...')
    return render(request,'insert_user.html',d) 

def insert_order(request):
    EOFO=OrderForm()
    d={'EOFO':EOFO}

    if request.method=='POST':
        OFDO=OrderForm(request.POST)
        if OFDO.is_valid():
            OFDO.save()
            return HttpResponse('insert order is Done Successfully...')
    return render(request,'insert_order.html',d)