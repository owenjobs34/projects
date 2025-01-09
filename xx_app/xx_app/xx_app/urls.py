"""
URL configuration for xx_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from xxapp import views 

urlpatterns = [
    path('', views.home, name='xxapp'),
    path("watch_video/<int:video_id>/", views.watch_video, name="watch_video"),
    path('upload_video/<int:channel_id>/', views.video_upload, name='upload_video'),
    path("channel/<int:channel_id>/", views.channel, name="channel"),
    path('create_channel',views.channel_create, name='channel_create'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('admin/', admin.site.urls),
]
