from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video, Proj, Relation_proj, Relation_tag, Relation_comment

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
    return render(request, 'video.html', {'video': video})

def proj(request, proj_id):
    proj = get_object_or_404(Proj, pk=proj_id)
    videos_list = []
    context = {
        'proj': proj,
        'videos_list': videos_list,
    }
    return render(request, 'proj.html', context)
