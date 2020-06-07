from django.shortcuts import render
from django.http import HttpResponse
from .models import Userandpass
# Create your views here.

def userandpass(request):
    uandp = Userandpass.objects.all()
    return render(request, 'userandpass.html', {'userandpass':userandpass})
