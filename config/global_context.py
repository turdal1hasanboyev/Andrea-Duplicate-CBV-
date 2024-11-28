from apps.article.models import Article, Category, Tag

def custom_global_context(request):
    popular_articles = Article.objects.all().order_by('-views')[:3]
    categories = Category.objects.all().order_by('name')
    tags = Tag.objects.all().order_by('name')

    context = {
        'popular_articles': popular_articles,
        'categories': categories,
        'tags': tags,
    }
    
    return context