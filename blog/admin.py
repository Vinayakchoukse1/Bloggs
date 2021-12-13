from operator import pos
from django.contrib import admin
from .models import Post, Comment, Image

class ImageAdmin(admin.StackedInline):
    model=Image

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    list_display = ('author', 'title')
    fieldsets = [
        (None, { 'fields': [('title','text', 'created_date', 'published_date', 'images')] } ),
    ]

    def save_model(self, request, obj, form, chang):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Image)

