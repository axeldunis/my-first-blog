from django.urls import path
from . import views

urlpatterns = [
  path('Home.html/', views.home, name='home'), 
  path('Netflix.html/', views.netflix, name='netflix'),  
  path('Prime_video.html/', views.prime, name='prime_video'), 
  path('Paramount_plus.html/', views.paramount, name='paramount_plus'), 
]
