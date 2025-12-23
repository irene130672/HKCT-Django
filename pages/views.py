from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request,request.path)
    return render(request,'pages/index.html')
# HttpResponse means show 
def about(request):
    print(request,request.path)
    return HttpResponse("<h1>about</h1>")
def about(request):
    return render(request,'pages/about.html')