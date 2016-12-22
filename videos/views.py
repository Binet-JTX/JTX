from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

n_page = 4
n_index = 5

def index(request):
    projs = Proj.objects.filter(category__public=True)
    videos = Video.objects.filter(public=True)
    categories = Category.objects.filter(public=True)
    if (request.user.is_authenticated):
        projs = Proj.objects
        videos = Video.objects
        categories = Category.objects
    context = {
        'request': request,
        'projs': projs.order_by('date').all()[:n_index],
        'videos': videos.order_by('date').all()[:n_index],
        'categories': categories.all()[:n_index],
    }
    return render(request, 'index.html', context)

def categories(request):
    categories = Category.objects.filter(public=True).all()
    if (request.user.is_authenticated):
        categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)

def category(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    if cat.public or request.user.is_authenticated:
        projs = Proj.objects.filter(category=cat)
        context = {
            'category': cat,
            'projs': projs,
        }
        return render(request, 'category.html', context)
    return index(request)

def projs(request, page=1):
    projs = Proj.objects.filter(category__public=True)
    if (request.user.is_authenticated):
        projs = Proj.objects
    page = int(page)
    nb_page = ((projs.count() - 1) // n_page) + 1
    projs = projs.all()[(page - 1) * n_page:page * n_page]
    context = {
        'page': page,
        'pages': range(1, nb_page + 1),
        'projs': projs,
    }
    return render(request, 'projs.html', context)

def proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)
    if proj.category.public or request.user.is_authenticated:
        proj.views += 1
        proj.save()
        context = {
            'proj': proj,
        }
        return render(request, 'proj.html', context)
    return index(request)

def favorites(request, page=1):
    if (request.user.is_authenticated):
        user = request.user
        favorites = Favorite.objects.filter(user = user)
        page = int(page)
        nb_page = ((favorites.count() - 1) // n_page) + 1
        favorites = favorites.all()[(page - 1) * n_page:page * n_page]
        context = {
            'page': page,
            'pages': range(1, nb_page + 1),
            'favorites': favorites,
        }
        return render(request, 'favorites.html', context)
    else:
        return index(request)

def videos(request, page=1):
    videos = Video.objects.filter(public=True)
    if (request.user.is_authenticated):
        videos = Video.objects
    page = int(page)
    nb_page = ((videos.count() - 1) // n_page) + 1
    videos = videos.all()[(page - 1) * n_page:page * n_page]
    context = {
        'page': page,
        'pages': range(1, nb_page + 1),
        'videos': videos,
    }
    return render(request, 'videos.html', context)

def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    if video.public or request.user.is_authenticated:
        video.views += 1
        video.save()
        n = Favorite.objects.filter(video = video).count()
        favorite = False
        if (request.user.is_authenticated):
            user = request.user
            favorite = Favorite.objects.filter(user = user, video = video).exists()
        context = {
            'video': video,
            'favorite': favorite,
            'nb_jaimes': n,
        }
        return render(request, 'video.html', context)
    return index(request)

def tags(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'tags.html', context)

def tag(request, tag_id):
    #TODO : À modifier pour public
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'tag.html', {'tag': tag})

def remove_favorite(request, video_id):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, pk=video_id)
        user = request.user
        c = Favorite.objects.filter(user = user, video = video).delete()
    return HttpResponseRedirect(reverse('videos:video', args=(video.id,)))

def add_favorite(request, video_id):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, pk=video_id)
        user = request.user
        c = Favorite(user = user, video = video)
        c.save()
    return HttpResponseRedirect(reverse('videos:video', args=(video.id,)))

def comment_video(request, video_id):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, pk=video_id)
        comment = request.POST['comment']
        user = request.user
        c = Relation_comment(author = user, video = video, comment = comment)
        c.save()
    return HttpResponseRedirect(reverse('videos:video', args=(video.id,)))

def comment_proj(request, proj_id):
    if request.user.is_authenticated:
        proj = get_object_or_404(Proj, pk=proj_id)
        comment = request.POST['comment']
        user = request.user
        c = Relation_comment_proj(author = user, proj = proj, comment = comment)
        c.save()
    return HttpResponseRedirect(reverse('videos:proj', args=(proj.id,)))
