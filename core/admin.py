# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Carousel, Label, Album, Category, Upload, Pricing, Team

# Register your models here.


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'message']


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'slug']


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['image', 'label', 'category', 'album']


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['price', 'title', 'description']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'message']


