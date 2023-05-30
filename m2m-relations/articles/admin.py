from django.contrib import admin

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']

@admin.register(Scope)
class AdminScope(admin.ModelAdmin):
    list_display = ['is_main', 'articles', 'tag']