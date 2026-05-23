from django.urls import path
from .views import BlogListView
from .views import BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='post-list'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),   
]