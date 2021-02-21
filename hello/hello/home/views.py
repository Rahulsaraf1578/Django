from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context = {
        "variables":'This is a rock',
        "naming":'This is the sexy variable'
    }
    messages.success(request,'this is a test message')
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("This is about")

def icecream(request):
    return render(request,'icrcream.html')

def softy(request):
    return render(request,'softy.html')

def familypack(request):
    return render(request,'familypack.html')

def contact(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        email =  request.POST.get('email')
        phone =  request.POST.get('phone')
        desc =  request.POST.get('desc')
        contact = Contact(name = 'name',email = 'email',phone='phone',desc = 'desc',date = datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')

    return render(request,'contact us.html')