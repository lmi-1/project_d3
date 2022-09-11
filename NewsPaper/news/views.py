from django.views.generic import ListView, DetailView
from .models import Post

class PostsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_news'] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'
