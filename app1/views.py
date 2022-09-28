from django.contrib import messages
from django.contrib.messages import constants as messages
#from app1.models import jobs, sample_table
from django.contrib import messages
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    return render(request,'new.html')
def course(request):
    return render(request,'course.html')
def coursedetail(request):
        return render(request,'course-detail.html')
def gallery(request):
        return render(request,'gallery.html')
def blogarchive(request):
        return render(request,'blog-archive.html')
def blogsingle(request):
        return render(request,'blog-single.html')
def contact(request):
        return render(request,'contact.html')

def index2(request):
    name = slidepicture.objects.all()
    vid = video.objects.all()
    modelt= modelteacher.objects.all()
    par= partner.objects.all()
    return render(request,'new.html', {'name': name, 'vid': vid, 'modelt': modelt, 'par': par} )