from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from . import views
from app1.views import index,index2

urlpatterns = [
  
    path('', views.index2, name='index2'),
    path('new.html', views.index2, name='home'),
    path('course.html', views.course, name='course'),
    path('course-detail.html', views.coursedetail, name='course-detail'),
    path('gallery.html', views.gallery, name='gallery'),
    path('blog-archive.html', views.blogarchive, name='blog-archive'),
    path('blog-single.html', views.blogsingle, name='blog-single'),
    path('contact.html', views.contact, name='contact'),
    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
