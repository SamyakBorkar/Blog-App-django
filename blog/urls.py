from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='blog-home'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_create, name='post-create'),
    path('post/<int:post_id>/edit/', views.post_update, name='post-update'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post-delete')
]