from django.contrib import admin
from .models import Video, Proj, Relation_proj, Relation_tag, Relation_comment

admin.site.register(Video)
admin.site.register(Proj)
admin.site.register(Relation_proj)
admin.site.register(Relation_tag)
admin.site.register(Relation_comment)
