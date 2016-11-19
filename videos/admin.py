from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Relation_proj)
admin.site.register(Relation_comment)
admin.site.register(Relation_comment_proj)

# --------------------
# --------------------
# Video
# --------------------
# --------------------

class TagInline(admin.TabularInline):
    model = Relation_tag
    extra = 0

class VideoAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date', 'views', 'public']
    list_filter = ['date', 'views', 'public']
    search_fields = ['titre']
    fieldsets = [
        (None, {'fields' : ['url', 'titre', 'public']}),
        ('Date and views', {'fields' : ['date', 'views'], 'classes' : ['collapse']}),
    ]
    inlines = [TagInline]

admin.site.register(Video, VideoAdmin)

# --------------------
# --------------------
# Proj
# --------------------
# --------------------

class VideoInline(admin.TabularInline):
    model = Relation_proj
    extra = 0

class ProjAdmin(admin.ModelAdmin):
    list_display = ['titre', 'category', 'date', 'views']
    list_filter = ['category', 'date', 'views']
    search_fields = ['titre', 'category__titre']
    fieldsets = [
        (None, {'fields' : ['category', 'titre']}),
        ('Date and views', {'fields' : ['date', 'views'], 'classes' : ['collapse']}),
    ]
    inlines = [VideoInline]

admin.site.register(Proj, ProjAdmin)

# --------------------
# --------------------
# Category
# --------------------
# --------------------

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['titre', 'public']
    list_filter = ['public']
    search_fields = ['titre']

admin.site.register(Category, CategoryAdmin)
