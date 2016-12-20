from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'videos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^projs/$', views.projs, name='projs'),
    url(r'^videos/$', views.videos, name='videos'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^projs/(?P<proj_id>[0-9]+)/$', views.proj, name='proj'),
    url(r'^videos/(?P<video_id>[0-9]+)/$', views.video, name='video'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', views.tag, name='tag'),
    url(r'^favorite/(?P<video_id>[0-9]+)/$', views.favorite, name='favorite'),
    url(r'^comment_video/(?P<video_id>[0-9]+)/$', views.comment_video, name='comment_video'),
    url(r'^comment_proj/(?P<proj_id>[0-9]+)/$', views.comment_proj, name='comment_proj'),
]
