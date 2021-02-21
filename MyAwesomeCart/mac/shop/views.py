from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("This is contact end point")

def tracker(request):
    return HttpResponse("This is tracker end point")

def search(request):
    return HttpResponse("This is search end point")

def productView(request):
    return HttpResponse("This is productView end point")

def checkout(request):
    return HttpResponse("This is checkout end point")