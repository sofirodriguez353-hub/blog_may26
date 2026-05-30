from django.shortcuts import render
from .models import Blog
from django.views.generic import (
                                    DetailView,
                                    ListView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                    )
from django.urls import reverse_lazy    

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

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'post-update.html'
    fields = ['title', 'content']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'post-delete.html'
    success_url = reverse_lazy('post-list')