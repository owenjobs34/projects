from django.db import models 
from django.contrib.auth.models import User 


class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    banner_image = models.URLField(max_length=200, blank=True)
    subscribers = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models.DurationField() # Adding a duration field
    #video_file = models.FileField(upload_to='videos/') 
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    privacy_status = models.BooleanField(default=False) # Adding a boolean field

    def __str__(self): 
        return self.title
