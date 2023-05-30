from django.shortcuts import render

from articles.models import Article, Tag, Scope


def articles_list(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    scopes = Scope.objects.all()
    template = 'articles/news.html'
    context = {
        'articles': articles,
        'tags': tags,
        'scopes': scopes,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
