from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Relation_proj)
admin.site.register(Relation_comment)
admin.site.register(Relation_comment_proj)

class TagInline(admin.StackedInline):
    model = Relation_tag
    extra = 0

class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['url', 'titre', 'public']}),
        ('Date and views', {'fields' : ['date', 'views'], 'classes' : ['collapse']}),
    ]
    inlines = [TagInline]

admin.site.register(Video, VideoAdmin)

class VideoInline(admin.StackedInline):
    model = Relation_proj
    extra = 0

class ProjAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['category', 'titre']}),
        ('Date and views', {'fields' : ['date', 'views'], 'classes' : ['collapse']}),
    ]
    inlines = [VideoInline]

admin.site.register(Proj, ProjAdmin)
