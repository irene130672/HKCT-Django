from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pages/index.html')
# HttpResponse means show 
def about(request):
    return HttpResponse("<h1>about</h1>")
def about(request):
    return render(request,'pages/about.html')