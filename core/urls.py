"""Litt URL Configuration

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
# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
# from .views import HomeView
from . import views

app_name = 'core'

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', views.index, name='index',),
    path('Home', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('category/<slug>', views.category_detail, name='category_detail'),
    path('albums/', views.album, name='album'),
    path('albums/<slug>', views.album_detail, name='album_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('pricing/', views.pricing, name='price'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.send_success, name='send_success'),

]
