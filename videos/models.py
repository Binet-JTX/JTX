from __future__ import unicode_literals

from django.db import models

class Video(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateTimeField()
    url = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    def __unicode__(self):
        return self.titre

class Tag(models.Model):
    titre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.titre

class Category(models.Model):
    titre = models.CharField(max_length=100)
    public = models.BooleanField(default=False)
    def __unicode__(self):
        return self.titre

class Proj(models.Model):
    titre = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    date = models.DateTimeField()
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.titre

class Relation_proj(models.Model):
    proj = models.ForeignKey(Proj)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.proj.titre + u" : " + self.video.titre

class Relation_tag(models.Model):
    tag = models.ForeignKey(Tag)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.video.titre + u" : " + self.tag.titre

class Relation_comment(models.Model):
    comment = models.CharField(max_length=1000)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.video.titre + u" : " + self.comment

class Relation_comment_proj(models.Model):
    comment = models.CharField(max_length=1000)
    proj = models.ForeignKey(Proj)
    def __unicode__(self):
        return self.proj.titre + u" : " + self.comment
