from django.shortcuts import render
from .models import CarouselImage,About,OurService,Room,AboutVideo,Benefit

# Create your views here.

def home(request):
    carousel_images = CarouselImage.objects.all()
    about_us = About.objects.get()
    our_services = OurService.objects.all()
    room = Room.objects.all()
    context = {'carousel_images':carousel_images, 'about_us': about_us, 'our_services': our_services, 'room': room}
    return render(request, 'base/home.html', context)


def about(request):
    about_video = AboutVideo.objects.get()
    about_us = About.objects.get()
    benefits = Benefit.objects.all()
    context = {'about_video':about_video, 'about_us':about_us, 'benefits': benefits}
    return render(request,'base/about.html',context)