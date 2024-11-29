from django.views.generic import TemplateView

class CustomPageNotFoundPageView(TemplateView):
    template_name = '404.html'

    def render_to_response(self, context, **kwargs):
        response = super().render_to_response(context, **kwargs)
        response.status_code = 404
        return response