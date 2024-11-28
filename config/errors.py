from django.views.generic import TemplateView

class CustomPageNotFoundPageView(TemplateView):
    template_name = '404.html'