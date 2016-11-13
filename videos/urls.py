from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<proj_id>[0-9]+)/$', views.proj, name='proj'),
    url(r'^video/(?P<video_id>[0-9]+)/$', views.video, name='video'),
]
