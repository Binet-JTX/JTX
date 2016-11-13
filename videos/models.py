from __future__ import unicode_literals

from django.db import models

class Video(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateTimeField()
    url = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class Proj(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateTimeField()
    public = models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class Relation_proj(models.Model):
    proj = models.ForeignKey(Proj)
    video = models.ForeignKey(Video)
    def __str__(self):
        return self.proj.titre + " : " + self.video.titre

class Relation_tag(models.Model):
    tag = models.CharField(max_length=100)
    video = models.ForeignKey(Video)
    def __str__(self):
        return self.video.titre + " : " + self.tag

class Relation_comment(models.Model):
    comment = models.CharField(max_length=1000)
    video = models.ForeignKey(Video)
    def __str__(self):
        return self.video.titre + " : " + self.comment
