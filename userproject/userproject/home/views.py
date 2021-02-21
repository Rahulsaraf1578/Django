from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password2 == password1:
            if User.objects.filter(username=username).exists( ):
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists( ):
                messages.info(request,'Email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'User created')
                return render(request,'login.html')
        else:
            messages.info(request,'Password not matching')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/')

    else:
        return render(request,"login.html")


