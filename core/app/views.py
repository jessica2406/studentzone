from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.
def base(request):
    return render(request,'base.html')
def home(request):
    events = Event.objects.all()  
    return render(request,'home.html', {'events': events})

def login(request):
    return render(request,'login.html')
