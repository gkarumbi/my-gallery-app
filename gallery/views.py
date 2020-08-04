from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
import datetime as dt

# Create your views here.

def my_photos(request):
    photos = Image.objects.all()

    return render(request,'welcome.html',{'photos':photos})
