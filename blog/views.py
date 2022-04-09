from django.shortcuts import render
from django.views import generic
from .models import BlogPost
from .forms import PostForm
from django.urls import reverse_lazy
class ShowListView (generic.ListView):

    template_name = 'blog/post_view.html'
    context_object_name = 'post'
    def get_queryset(self):
        return BlogPost.objects.filter(status='p').order_by('-datetime_created')


class ShowDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class AddPostView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #success_url = reverse_lazy('detail')



class EditPost(generic.UpdateView):
    model=BlogPost
    form_class = PostForm
    template_name = 'blog/update_post.html'

    #success_url = reverse_lazy('detail')

class Deletpost(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog list')
