from django.urls import path
from .views import (
                    BlogListView, 
                    BlogDetailView, 
                    BlogCreateView, 
                    BlogUpdateView,)


urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/crear/', BlogCreateView.as_view(), name='post-crear'),
    path('post/actualizar/<int:pk>/', BlogUpdateView.as_view(), name='post-update'),
]