# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.


class Carousel(models.Model):
    image = models.ImageField( upload_to='carousel/')
    status = models.BooleanField( blank=True, null=True, default=False)
    title = models.CharField( max_length=50, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = _("Carousel")
        verbose_name_plural = _("Carousel")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Carousel_detail", kwargs={"pk": self.pk})


class Label(models.Model):
    name = models.CharField( max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Label")
        verbose_name_plural = _("Labels")

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField( max_length=50, blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("Album_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True, default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:Category", kwargs={"pk": self.pk})


class Upload(models.Model):
    image = models.FileField(upload_to='uploads/')
    label = models.ForeignKey("core.Label", on_delete=models.DO_NOTHING, max_length=200, blank=True, null=True)
    category = models.ForeignKey("core.Category", on_delete=models.DO_NOTHING, max_length=200, blank=True, null=True )
    album = models.ForeignKey("core.Album", on_delete=models.DO_NOTHING, max_length=200, blank=True, null=True )
    date = models.DateField( auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("upload")
        verbose_name_plural = _("uploads")

    def __str__(self):
        return self.image.name

    def get_absolute_url(self):
        return reverse("core:uploads", kwargs={"pk": self.pk})


class Pricing(models.Model):
    
    image = ImageField(upload_to='pricing/', max_length=100)
    price = models.IntegerField(blank=True,null=True)
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = _("pricing")
        verbose_name_plural = _("pricings")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:pricing", kwargs={"pk": self.pk})


class Team(models.Model):
    image = models.ImageField( upload_to='team/')
    status = models.BooleanField( blank=True, null=True, default=True)
    name = models.CharField( max_length=50, blank=True, null=True)
    title = models.CharField( max_length=50, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name


