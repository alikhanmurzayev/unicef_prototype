from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile_detail_view, name='profile_detail'), 
    
]

