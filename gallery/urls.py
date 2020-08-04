from  django.conf import settings
from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    url(r'^', views.my_photos, name = 'my-photos'),
    url(r'^images/(\d+)', views.my_photo,name='my-photo'),
    url(r'^search/', views.search_results,name='results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)