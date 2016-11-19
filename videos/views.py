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

    # Create a relation_comment
    return HttpResponseRedirect(reverse('videos:video', args=(video.id,)))

def comment_proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)

    # Create a relation_comment_proj
    return HttpResponseRedirect(reverse('videos:proj', args=(proj.id,)))
