from django.shortcuts import render
from .models import CarouselImage,About

# Create your views here.

def home(request):
    carousel_images = CarouselImage.objects.all()
    about_us = About.objects.get()
    context = {'carousel_images':carousel_images, 'about_us': about_us}
    return render(request, 'base/home.html', context)