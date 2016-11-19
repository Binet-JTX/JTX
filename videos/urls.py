from django.conf.urls import url

from . import views

app_name = 'videos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<proj_id>[0-9]+)/$', views.proj, name='proj'),
    url(r'^video/(?P<video_id>[0-9]+)/$', views.video, name='video'),
    url(r'^comment_video/(?P<video_id>[0-9]+)/$', views.comment_video, name='comment_video'),
    url(r'^comment_proj/(?P<proj_id>[0-9]+)/$', views.comment_proj, name='comment_proj'),
]
