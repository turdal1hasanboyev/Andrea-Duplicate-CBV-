from django.shortcuts import render, redirect
from django.views import View
from .models import Contact


class ContactPageView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        url = request.build_absolute_uri()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        contact.save()
        return redirect(url)