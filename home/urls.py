from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('contact', views.ContactMeView.as_view(), name='contact_me'),
]
