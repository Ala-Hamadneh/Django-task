from django.shortcuts import render
from datetime import datetime

# Create your views here.

def page(request):
    context = {
        'message': 'Welcome to App2!',
        'current_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render(request, 'page.html', context)