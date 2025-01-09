from django import forms
 
# import GeeksModel from models.py
from .models import Channel, Video

class ChannelForms(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Channel
        fields = "__all__"

class VideoForms(forms.ModelForm):
    # specify the name of the model
    class Meta:
        model = Video
        fields = "__all__"