
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from xx_app import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from .models import Channel, Video
from .forms import ChannelForms, VideoForms
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.


def home(request):
    channel = Channel.objects.all()
    context = {"channel": channel
               }
    return render(request, 'xxapp/index.html', context)

def watch_video(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        "video": video
    }
    return render(request, 'xxapp/watch_video.html', context)

def video_upload(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    if request.method == "POST":
        form = VideoForms(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            duration = form.cleaned_data['duration']
            #upload_date = form.cleaned_data['upload_date']
            tags = form.cleaned_data['tags']
            category = form.cleaned_data['category']
            new_video = Video(channel=channel,creator=request.user,title=title,description=description,
                          duration=duration,tags=tags,category=category)
            new_video.save()
            print('done')
            return HttpResponseRedirect(reverse("channel", args=(channel.id,)))
        else:
            form = VideoForms()
            print('out')

    context = {
               "form": VideoForms()
        }
        
    return render(request, "xxapp/video_upload.html",  context)



def channel(request, channel_id):
    user = request.user
    my_channel = Channel.objects.get(user=user)
    channel = Channel.objects.get(id=channel_id)
    if my_channel:
        print('available')
    print(channel_id)
    context = {"channel": channel}
    return render(request, 'xxapp/channel.html', context)



def channel_create(request):
     if request.method == "POST":
         form = ChannelForms(request.POST)
         if form.is_valid():
             name = form.cleaned_data['name']
             description = form.cleaned_data['description']
             user = form.cleaned_data['user']
             user_id = request.user
             print(user_id)
             new_channel = Channel(name=name,description=description, user=user_id)
             new_channel.save()
             print(new_channel.id)
             
             return HttpResponseRedirect(reverse("channel", args=(new_channel.id,)))
         else:
            form = ChannelForms()
            print('out')

     
     
     context = {
         "form": ChannelForms()
     }
     return render(request, 'xxapp/channel_create.html', context)
    














def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.fname = fname
        myuser.lname = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
       
        
        return redirect('signin')
        
        
    return render(request, "xxapp/signup.html")


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')
    
def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            username = user.username
            return render(request,"xxapp/index.html", {'username' : username})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect("home")
    return render(request, "xxapp/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")