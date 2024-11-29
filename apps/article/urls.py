from django.urls import path
from .views import HomePageView, FashionPageView, TravelPageView, SinglePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('fashion/', FashionPageView.as_view(), name='fashion'),
    path('travel/', TravelPageView.as_view(), name='travel'),
    path('single/<slug:slug>/', SinglePageView.as_view(), name='single'),
]