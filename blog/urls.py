from django.urls import path
from . import views

urlpatterns = [
  path('',views.post_list,name='post_list'),
  path('post/<int:pk>/', views.post_detail, name='post_detail'),
  path('post/new/', views.post_new, name='post_new'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit'), 
  path('',views.page_accueil,name='Home'),
  path('',views.netflix,name='Netflix'),
  path('',views.prime,name='Prime_video'),
  path('',views.paramount,name='Paramount_plus'),
]
