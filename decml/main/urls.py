from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('thank-you/', views.thank_you, name='thank_you'),
    ]
