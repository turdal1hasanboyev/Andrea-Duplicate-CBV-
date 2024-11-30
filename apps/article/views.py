from django.shortcuts import redirect, render
from django.views.generic import ListView, TemplateView, DetailView
from apps.article.models import Article, Comment
from apps.common.models import SubEmail
from django.views import View


class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 12

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')

        queryset = Article.objects.all().order_by('id')

        if cat:
            queryset = queryset.filter(category__slug__iexact=cat)
        if tag:
            queryset = queryset.filter(tags__slug__iexact=tag)
        return queryset

    def post(self, request, *args, **kwargs):
        sub_email = request.POST.get('sub_email')

        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect('/')
    

class FashionPageView(TemplateView):
    template_name = 'fashion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(category__slug__iexact='fashion-dedba710-2bc6-4f2a-9d30-2401d24c490d').order_by('-id')[:12]
        return context

    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        sub_email = request.POST.get('sub_email')

        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect(url)
    

class TravelPageView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.filter(category__slug__exact='travel-a7bb8ce7-b703-4426-a5d5-a2bf4d30254f').order_by('id')

        context = {
            'articles': articles[:8],
        }
        return render(request, 'travel.html', context)
    
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        sub_email = request.POST.get('sub_email')
        
        if sub_email:
            SubEmail.objects.create(email=sub_email)
            return redirect(url)


class SinglePageView(DetailView):
    model = Article
    template_name = 'single.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        article = Article.objects.get(slug__iexact=slug)
        article.views =+ 1
        article.save()
        return article

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        sub_email = request.POST.get('sub_email')

        if sub_email:
            SubEmail.objects.create(email=sub_email)

        if not request.user.is_authenticated:
            return redirect("login")

        name = request.POST.get('name')
        email = request.POST.get('email')
        web_site = request.POST.get('web_site')
        message = request.POST.get('message')

        if name and email and web_site and message:
            Comment.objects.create(
            article_id=article.id,
            user_id=request.user.id,
            name=name,
            email=email,
            web_site=web_site,
            message=message,
        )
        return redirect(article.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        comments = Comment.objects.filter(article_id=article.id).order_by('-id')
        context['comments'] = comments
        return context