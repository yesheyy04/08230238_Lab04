from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # Home page
    path('index/', views.index, name='index'), # Learning Journey
    path('about/', views.aboutMe, name='about'), # About Me
]
