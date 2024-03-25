from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def hellword(request):
    return render(request,'Login/signup.html',{
        'form': UserCreationForm
    })