from django.urls import path
from . import views

urlpatterns = [
    path('CONTACT/', views.CONTACT, name='CONTACT'),
]