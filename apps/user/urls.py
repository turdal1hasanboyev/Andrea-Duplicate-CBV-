from django.urls import path
from .views import AboutPageView, LoginPageView, LogoutView, RegisterPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPageView.as_view(), name='register'),
]