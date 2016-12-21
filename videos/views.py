from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

def index(request):
    n = 4
    all_projs = Proj.objects.filter(category__public=True)
    if (request.user.is_authenticated):
        all_projs = Proj.objects
    latest_videos = Video.objects.filter(public=True)
    if (request.user.is_authenticated):
        latest_videos = Video.objects
    context = {
        'request': request,
        'projs': all_projs.order_by('date').all()[:n],
        'videos': latest_videos.order_by('date').all()[:n],
    }
    return render(request, 'index.html', context)

def projs(request):
    projs = Proj.objects.filter(category__public=True).all()
    if (request.user.is_authenticated):
        projs = Proj.objects.all()
    context = {
        'projs': projs,
    }
    return render(request, 'projs.html', context)


def tags(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'tags.html', context)

def favorites(request):
    if (request.user.is_authenticated):
        user = request.user
        favorites = Favorite.objects.filter(user = user).all()
        context = {
            'favorites': favorites,
        }
        return render(request, 'favorites.html', context)
    else:
        return index(request)

def videos(request):
    videos = Video.objects.filter(public=True).all()
    if (request.user.is_authenticated):
        videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos.html', context)

def tag(request, tag_id):
    #TODO : À modifier pour public
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'tag.html', {'tag': tag})

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

def proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)
    if proj.category.public or request.user.is_authenticated:
        proj.views += 1
        proj.save()
        videos_list = []
        context = {
            'proj': proj,
            'videos_list': videos_list,
        }
        return render(request, 'proj.html', context)
    return index(request)

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
