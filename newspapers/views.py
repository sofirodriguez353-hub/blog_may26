from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView, ListView, CreateView

# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name = 'post-list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post-detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'post-create.html'
    fields = ['title', 'content', 'author']