from django.views.generic import TemplateView

class CustomPageNotFoundView(TemplateView):
    template_name = '404.html'