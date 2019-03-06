
from django.views.generic import ListView,DetailView
from . models import Blog

class BlogListView(ListView):
    model=Blog
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Blog
    template_name='detail.html'
    context_object_name='batman'
