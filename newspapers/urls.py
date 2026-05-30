from django.urls import path
from .views import BlogListView
from .views import BlogDetailView
from .views import BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/crear/', BlogCreateView.as_view(), name='post-crear'),
]