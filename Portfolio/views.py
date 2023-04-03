from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.forms.models import model_to_dict
from django.utils import timezone

from . import models
from . import forms


def index(request):
    portfolio = get_object_or_404(models.Portfolio, pk='1')
    posts = []
    all_posts = models.Post.objects.all().order_by('-id')[:3]
    for post in all_posts:
        posts.append(post)
    return render(request, 'portfolio/index.html', {
                    'portfolio': portfolio,
                    'posts': posts
                    })

def gallery(request):
    """List all photos"""
    photos = []
    posts = []
    all_photos = models.Photo.objects.all().order_by('-id')
    portfolio = get_object_or_404(models.Portfolio, pk='1')
    for photo in all_photos:
        photos.append(photo)
    return render(request, 'portfolio/gallery.html', {
                    'photos': photos,
                    'portfolio': portfolio,
                    'posts': posts
                    })

def photo_upload(request):
    title = 'Upload Photo'
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.created_date = timezone.now()
            new_photo.save()
            return redirect('gallery')
    else:
        form = forms.PhotoForm()
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def photo_edit(request, pk):
    title = "Photo Edit"
    photo = get_object_or_404(models.Photo, pk=pk)
    form = forms.PhotoForm(instance=photo)
    if request.method == "POST":
        form = forms.PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('gallery')
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def photo_delete(request, pk):
    title = 'Delete Photo'
    post = get_object_or_404(models.Photo, pk=pk)
    post.delete()
    return redirect('gallery')

def expedition_list(request):
    """List all expeditions"""
    expeditions = []
    all_expeditions = models.Expedition.objects.all().order_by('-id')
    for expedition in all_expeditions:
        expeditions.append(expedition)
    return render(request, 'portfolio/expedition_list.html', {
            'expeditions': expeditions
            })

def expedition_detail(request, pk):
    expedition = model_to_dict(get_object_or_404(models.Expedition, pk=pk))
    photos = models.Photo.objects.all(
            ).filter(Q(expedition_id__exact=expedition['expedition_id']))
    posts = models.Post.objects.all(
            ).filter(Q(expedition_id__exact=expedition['expedition_id'])
            ).order_by('-id')
    return render(request, 'portfolio/expedition_detail.html',{
            "expedition": expedition,
            "photos": photos,
            "posts": posts
            })


def expedition_new(request):
    title = 'New Expedition'
    if request.method == "POST":
        form = forms.ExpeditionForm(request.POST, request.FILES)
        if form.is_valid():
            new_expedition = form.save(commit=False)
            new_expedition.created_date = timezone.now()
            new_expedition.save()
            return redirect('expeditions')
    else:
        form = forms.ExpeditionForm()
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def expedition_edit(request, pk):
    title = 'Edit Expedition'
    expedition = get_object_or_404(models.Expedition, pk=pk)
    form = forms.ExpeditionForm(instance=expedition)
    if request.method == "POST":
        form = forms.ExpeditionForm(request.POST, request.FILES, instance=expedition)
        if form.is_valid():
            expedition = form.save(commit=False)
            expedition.save()
            return redirect('expedition_detail', pk=expedition.pk)
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def expedition_delete(request, pk):
    title = 'Delete Expedition'
    post = get_object_or_404(models.Expedition, pk=pk)
    post.delete()
    return redirect('expeditions')

def article_list(request):
    """List the 10 most recent Blog Posts"""
    posts = []
    all_posts = models.Post.objects.all().order_by('-id')
    for post in all_posts:
        posts.append(post)
    return render(request, 'portfolio/article_list.html', {
                    'posts': posts
                    })

def article_detail(request, pk):
    post = model_to_dict(get_object_or_404(models.Post, pk=pk))
    photos = models.Photo.objects.all(
            ).filter(Q(article_id__exact=post['article_id']))
    return render(request, 'portfolio/article_detail.html',{
                    "post": post,
                    "photos": photos
                    })

def article_new(request):
    title = 'Submit an Article!'
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_date = timezone.now()
            form.save()
            return redirect('article_list')
    else:
        form = forms.PostForm()
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def article_edit(request, pk):
    title = 'Edit Post'
    post = get_object_or_404(models.Post, pk=pk)
    form = forms.PostForm(instance=post)
    if request.method == "POST":
        form = forms.PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('article_list')
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def article_delete(request, pk):
    title = 'Delete Post'
    post = get_object_or_404(models.Post, pk=pk)
    post.delete()
    return redirect('article_list')

def jeep(request):
    """List all expeditions"""
    jeeps = []
    all_jeeps = models.Jeep.objects.all()
    for jeep in all_jeeps:
        jeeps.append(jeep)
    return render(request, 'portfolio/jeep.html', {
                    'jeeps': jeeps
                    })

def jeep_detail(request, pk):
    jeep = model_to_dict(get_object_or_404(models.Jeep, pk=pk))
    photos = models.Photo.objects.all(
            ).filter(Q(tags__icontains=jeep['jeep_name']))
    posts = models.Post.objects.all(
            ).filter(Q(tags__icontains=jeep['jeep_name']))
    return render(request, 'portfolio/jeep_detail.html',{
                    "jeep": jeep,
                    "photos": photos,
                    "posts": posts
                    })

def jeep_new(request):
    title = 'Submit a New Build'
    if request.method == "POST":
        form = forms.JeepForm(request.POST, request.FILES)
        if form.is_valid():
            new_jeep = form.save(commit=False)
            new_jeep.created_date = timezone.now()
            new_jeep.save()
            return redirect('jeep')
    else:
        form = forms.JeepForm()
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def jeep_edit(request, pk):
    title = 'Edit Jeep'
    jeep = get_object_or_404(models.Jeep, pk=pk)
    form = forms.JeepForm(instance=jeep)
    if request.method == "POST":
        form = forms.JeepForm(request.POST, request.FILES, instance=jeep)
        if form.is_valid():
            jeep = form.save(commit=False)
            jeep.save()
            return redirect('jeep_detail', pk=jeep.pk)
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def jeep_delete(request, pk):
    title = 'Delete Post'
    post = get_object_or_404(models.Jeep, pk=pk)
    post.delete()
    return redirect('jeep')

def portfolio_detail(request, pk):
    """portfolio view"""
    portfolio = model_to_dict(get_object_or_404(models.Portfolio, pk=pk))
    return render(request, 'portfolio/portfolio_detail.html', {
                    'portfolio': portfolio
                    })

def portfolio_new(request):
    title = 'Submit a New Portfolio'
    if request.method == "POST":
        form = forms.PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            new_portfolio = form.save(commit=False)
            new_portfolio.save()
            return redirect('index')
    else:
        form = forms.PortfolioForm()
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })

def portfolio_edit(request, pk):
    title = 'Edit Portfolio'
    portfolio = get_object_or_404(models.Portfolio, pk=pk)
    form = forms.PortfolioForm(instance=portfolio)
    if request.method == "POST":
        form = forms.PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.save()
            return redirect('index')
    return render(request, 'portfolio/new.html', {
                    'form': form,
                    'title': title
                    })