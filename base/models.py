from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='img/%y/%m')
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    descriptive_info = models.CharField(blank=True)

    def __str__(self):
        return self.title
    
class OurService(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='img/%y/%m')
    
    def __str__(self):
        return self.title
    
class Room(models.Model):
    room_name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    bed = models.CharField(max_length=155)
    services = models.CharField(max_length=255)
    price = models.CharField(max_length=20)

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='img/%Y/%m')


class AboutVideo(models.Model):
    youtube_url = models.CharField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    video_bg_image = models.ImageField(upload_to='img/%y/%m')
    play_icon = models.ImageField(upload_to='img/%y/%m')


class Benefit(models.Model):
    title = models.CharField()