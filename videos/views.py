from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

def index(request):
    all_projs = Proj.objects.all()
    latest_videos = Video.objects.order_by('date')[:10]
    context = {
        'projs': all_projs,
        'videos': latest_videos,
    }
    return render(request, 'index.html', context)

def projs(request):
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


def videos(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos.html', context)



def tag(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    return render(request, 'tag.html', {'tag': tag})

def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    video.views += 1
    video.save()
    return render(request, 'video.html', {'video': video})

def proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)
    proj.views += 1
    proj.save()
    videos_list = []
    context = {
        'proj': proj,
        'videos_list': videos_list,
    }
    return render(request, 'proj.html', context)

def comment_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    comment = request.POST['comment']

    c = Relation_comment(video = video, comment = comment)
    c.save()
    return HttpResponseRedirect(reverse('videos:video', args=(video.id,)))

def comment_proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)
    comment = request.POST['comment']

    c = Relation_comment_proj(proj = proj, comment = comment)
    c.save()

    # Create a relation_comment_proj
    return HttpResponseRedirect(reverse('videos:proj', args=(proj.id,)))
