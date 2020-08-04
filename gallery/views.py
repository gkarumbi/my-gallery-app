from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image
import datetime as dt

# Create your views here.

def my_photos(request):
    photos = Image.objects.all()

    return render(request,'welcome.html',{'photos':photos})

def my_photo(request, photo_id):
    photo = Image.objects.get(id=photo_id)

    return render(request,'photo.html',{'photo':photo})


def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Image.search_by_category(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{'message':message, 'photos':searched_photo})