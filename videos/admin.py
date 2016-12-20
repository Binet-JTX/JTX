from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Tag)
admin.site.register(Relation_proj)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'first_name', 'last_name']

class CommentProjAdmin(admin.ModelAdmin):
    list_display = ['comment', 'proj', 'date']
    list_filter = ['proj', 'date']
    search_fields = ['comment', 'proj__titre']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'video', 'date']
    list_filter = ['video', 'date']
    search_fields = ['comment', 'video__titre']

admin.site.register(Relation_comment, CommentAdmin)
admin.site.register(Relation_comment_proj, CommentProjAdmin)

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
