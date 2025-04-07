from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')


def base(request):
    return render(request,'base.html')

def about(request):
    return HttpResponse("<h1>About Page</h1>")
