"""iframe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

if settings.DEBUG:
    urlpatterns = [
        url(r'^register/$', views.UserCreateView.as_view(), name='register'),
        url(r'^profile/(?P<slug>[-\w]+)/$', views.UserDetailView.as_view(), name='profile'),
        url(r'^profile/edit/(?P<slug>[-\w]+)/$', views.UserAndProfileUpdateView.as_view(), name='edit'),
        url(r'^profile/(?P<slug>[-\w]+)/edit/password/$', views.update_password, name='edit-password'),


    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
