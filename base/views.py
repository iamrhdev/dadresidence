from django.shortcuts import render
from .models import CarouselImage,About,OurService,Room,AboutVideo,Benefit,ExtraService,DadResidenceDetail,GalleryImage

# Create your views here.

def home(request):
    carousel_images = CarouselImage.objects.all()
    about_us = About.objects.get()
    our_services = OurService.objects.all()
    room_details = Room.objects.all()
    details_residence = DadResidenceDetail.objects.get()
    context = {'carousel_images':carousel_images, 'about_us': about_us, 'our_services': our_services, 'room': room_details, 'details':details_residence}
    return render(request, 'base/home.html', context)


def about(request):
    about_video = AboutVideo.objects.get()
    about_us = About.objects.get()
    benefits = Benefit.objects.all()
    details_residence = DadResidenceDetail.objects.get()
    extras = ExtraService.objects.all()
    context = {'about_video':about_video, 'about_us':about_us, 'benefits': benefits, 'extras': extras, 'details':details_residence}
    return render(request,'base/about.html',context)

def room(request):
    room = GalleryImage.objects.all()
    details_residence = DadResidenceDetail.objects.get()
    context = {'room':room,'details':details_residence}
    return render(request, 'base/room.html', context)

def navbar(request):
    details_residence = DadResidenceDetail.objects.get()
    about = About.objects.get()
    context = {'details':details_residence,'about_us':about}
    return render(request, 'navbar.html', context)

def contact(request):
    details_residence = DadResidenceDetail.objects.get()
    context = {'details': details_residence}
    return render(request,'base/contact.html',context)