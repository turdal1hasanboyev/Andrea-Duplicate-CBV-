from django.views.generic import TemplateView
from .models import User


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user = User.objects.get(id=1)
        
        context['user'] = user
        
        return context