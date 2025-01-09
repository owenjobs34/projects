from django.db import models 
from django.contrib.auth.models import User 


class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(2000)
    banner_image = models.URLField(max_length=200, blank=True)
    subscribers = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    duration = models
    video_file = models.FileField(upload_to='videos/') 
    upload_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    privacy_status = models
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    comments = models.TextField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    channel_id = models.ForeignKey(Channel, on_delete=models.CASCADE)
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    streaming_urls = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title


class Comment(models.Model):
    video_id = models
    user_id = models
    text = models
    timestamp = models
    replies = models

class Subscription(models.Model):
    user_id = models
    channel_id = models

class Like_Dislike(models.Model):
    user_id = models
    video_id = models
    like = models

class Tag(models.Model):
    name = models
    videos = models

class Playlist(models.Model):
    user_id = models
    name = models
    description = models
    videos = models
