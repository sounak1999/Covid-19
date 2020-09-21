from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home-page'),
    #path('page2/', views.home, name = 'new-page'),
]
