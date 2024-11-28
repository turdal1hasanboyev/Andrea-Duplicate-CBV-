from django.shortcuts import redirect
from django.views.generic import ListView
from apps.article.models import Article
from apps.common.models import SubEmail


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
        query = request.POST.get('query')
        
        if sub_email:
            SubEmail.objects.create(email=sub_email)

        return redirect('/')