from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog_app.models import Comments,Posts
from blog_app.forms import CommentForm,PostForm
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostView(ListView):
    model = Posts
    def get_queryset(self):
        return Posts.objects.filter(published__lte=timezone.now())

class PostDetailView(DetailView):
    model = Posts

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    login_url = '/login/'
    redirect_field_name = 'posts_detail.html'
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Posts
    login_url = '/login/'
    redirect_field_name = 'posts_detail.html'
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Posts
    success_url= reverse_lazy('posts_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/posts_list.html'

    model = Posts

    def get_queryset(self):
        return Posts.objects.filter(published__isnull=True).order_by('created')

#####Start of the comments section #######

@login_required
def posts_publish(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    post.publish()
    return redirect('posts_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog_app/comments_form.html', {'form': form})
