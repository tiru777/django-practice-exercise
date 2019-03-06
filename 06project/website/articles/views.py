
from django.views.generic import ListView,DetailView
from . models import Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


class BlogListView(ListView):
    model=Blog
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Blog
    template_name='detail.html'
    context_object_name='batman'

class BlogCreateView(CreateView):
    model=Blog
    template_name='blog_create.html'
    fields = '__all__'  #what ever fields in blog model  we should import here
class BlogUpdateView(UpdateView):
    model=Blog
    template_name='blog_update.html'
    fields = ['title','text']  #we can call individual also
class BlogDeleteView(DeleteView):
    model=Blog
    template_name='blog_delete.html'
    context_object_name='batman'
    success_url = reverse_lazy ('home')
