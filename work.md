Men admin.py fayli uchun modellar registratsiyasini oddiy usulda yozmoqchiman (admin.site.register())
Paginator dan vos kechilmoqda
```python
from django.views import View
from django.shortcuts import render

class CustomPageNotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)
```
Aslida errors.py shunday yozilishi kerak edi.