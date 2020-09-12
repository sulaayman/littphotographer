# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.forms import ContactForm
from .models import Upload, Category, Album, Pricing, Team


# Create your views here.


# class HomeView(ListView):
#     model = Upload
#     paginate_by = 10
#     template_name = "home.html"


def index(request):
    upload_list = Upload.objects.all()

    context = {
        'upload_list': upload_list,
    }
    return render(request, 'index.html', context)


def about(request):
    teams = Team.objects.all().order_by('id')

    return render(request, 'about.html', {'teams':teams})


def home(request):
    upload_list = Upload.objects.all()
    category = Category.objects.filter(status=True)
    cat, t = [], []
    for c in category:
        u = upload_list.filter(category_id=c.id).order_by('id').first()
        cont = {
            'id': u.id,
            'image': u.image,
            'label': u.label,
            'category': u.category,
            'album': u.album,
        }
        t.append(u)  # [c.name, u]})
        cat.append(c)

    zipped = zip(cat, t)

    context = {
        'upload_list': upload_list,
        'category': category,
        'zipped': zipped
    }

    return render(request, 'home.html', context)


def category(request):

    category = Category.objects.filter(status=True)
    upload_list = Upload.objects.all()
    cat, t = [], []

    for c in category:
        u = upload_list.filter(category_id=c.id).order_by('id').first()

        t.append(u)
        cat.append(c)

    zipped = zip(cat, t)

    context = {
        'zipped': zipped,
    }

    return render(request, 'category.html', context)


def category_detail(request, slug):
    global title
    cat = Upload.objects.filter(category__slug=slug).order_by('date')
    for x in cat:
        title = x.category

    context = {
        'cat': cat,
        'title': title
    }

    return render(request, 'category_details.html', context)



def portfolio(request):
    album = Album.objects.all()
    category = Category.objects.filter(status=True)
    upload_list = Upload.objects.all()
    cat, t, a, new = [], [], [], []

    for c in category:
        u = upload_list.filter(category_id=c.id).order_by('id').first()
        cont = {
            'id': u.id,
            'image': u.image,
            'label': u.label,
            'category': u.category,
            'album': u.album,
        }
        t.append(u)  # [c.name, u]})
        cat.append(c)

    for r in album:
        u = upload_list.filter(album_id=r.id).order_by('id').last()
        cont = {
            'id': u.id,
            'image': u.image,
            'label': u.label,
            'category': u.category,
            'album': u.album,
        }
        new.append(u)  # [c.name, u]})
        a.append(r)

    zipped = zip(cat, t)
    zipped2 = zip(a, t)

    context = {
        'cat': cat,
        'album': album,
        'zipped': zipped,
        'zipped2': zipped2
    }

    return render(request, 'portfolio.html', context)


def album(request):
    album = Album.objects.all()
    upload_list = Upload.objects.all()
    a, new = [], []

    for r in album:
        u = upload_list.filter(album_id=r.id).order_by('id').last()
        cont = {
            'id': u.id,
            'image': u.image,
            'label': u.label,
            'category': u.category,
            'album': u.album,
        }
        new.append(u)  # [c.name, u]})
        a.append(r)

    zipped2 = zip(a, new)

    context = {
        'zipped2': zipped2
    }

    return render(request, 'album.html', context)


def album_detail(request, slug):
    global title
    ab= Upload.objects.filter(album__slug=slug).order_by('date')
    lim = ab[:5]
    for x in ab:
        title = x.album

    context = {
        'album': ab,
        'title': title,
        'x': lim,
    }

    return render(request, 'album_details.html', context)


def pricing(request):
    price = Pricing.objects.all().order_by('title')

    return render(request, 'pricing.html', {'price':price})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['bolaji635@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('core:send_success')

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def send_success(request):
    return HttpResponse('thanks you for you email ^_^')

