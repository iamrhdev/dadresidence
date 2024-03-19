from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='img/%y/%m')
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=255)  
    
    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title