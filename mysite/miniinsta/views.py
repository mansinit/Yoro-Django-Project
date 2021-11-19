# Create your views here.
from django.forms.widgets import Textarea
from django.http import HttpResponse
import os
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadFileForm, ImageForms
from .models import Pictures,Albums, upload_to
from django.core.files.storage import FileSystemStorage
def index(request):
    return HttpResponse("Hello, world. You're at my instagram page")


def album(request):
    
    form = UploadFileForm()
    album_name=Albums.objects.all()

    if "add_category" in request.POST:
        #album_name=Albums.objects.all()
        form = UploadFileForm(request.POST)
        form.save()
        for photo in album_name:
            dir = os.path.join(settings.MEDIA_ROOT,photo.album)
            if not os.path.exists(dir):
                os.mkdir(dir)
        form=UploadFileForm()

    return render(request, "miniinsta/home.html", context={'album_name':album_name,'form':form})


def view_photo(request,category):
    form = UploadFileForm()
    album_name=Albums.objects.all()
    if "view_photo" in request.POST:
        form_photo = ImageForms(request.POST, request.FILES)
        value=request.POST["view_photo"]
        pictures=Pictures.objects.filter(image__contains=category).all()
        
        if form_photo.is_valid():
            form_photo.save()
        return render(request=request, template_name="miniinsta/done.html", context={'form_photo': form_photo, 'posts': pictures})

    elif ("add_photo") in request.POST:
        form_photo = ImageForms(request.POST, request.FILES)
        #print(form_photo.image)
        
        #photo=request.FILES[0]
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(os.path.join(category,myfile.name), myfile)
        print(filename)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        #pictures = Pictures.objects.all()
        pictures_created = Pictures.objects.create(image=uploaded_file_url)
        pictures=Pictures.objects.filter(image__contains=category).all()
        print(pictures)
        #category1=Albums.objects.get(album=category)
        #pictures.get_category()
        if form_photo.is_valid():
            form_photo.save()

        
        return render(request=request, template_name="miniinsta/done.html", context={'form_photo': form_photo, 'posts': pictures})

    
def addphoto(request):
     if request.method == "POST":
        form_photo = ImageForms(request.POST, request.FILES)
        pictures = Pictures.objects.all()

        if form_photo.is_valid():
            form_photo.save()
        return render(request=request, template_name="miniinsta/home.html", context={'form_photo': form_photo, 'posts': pictures})


def upload(request):
    if request.method == "POST":
        form = ImageForms(request.POST, request.FILES)
        movies = Pictures.objects.all()

        if form.is_valid():
            form.save()
        return render(request=request, template_name="miniinsta/done.html", context={'form': form, 'posts': movies})

    form = ImageForms(request.POST)
    movies = Pictures.objects.all()

    return render(request=request, template_name="miniinsta/upload.html", context={'form': form, 'movies': movies,'n':1})


# from django.http import HttpResponseRedirect

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

'''def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})'''
