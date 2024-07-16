from django.urls import path, include
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('items/', include('MainApp.urls')),
]
