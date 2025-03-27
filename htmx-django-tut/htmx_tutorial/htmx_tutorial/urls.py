from django.urls import path
from . import views

urlpatterns = [
    path('', views.example, name='example'),
    path('', views.sample_post, name='sample-post'),
]