from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Home page
def home(request):
    # Data passed
    context = {
        'posts': Post.objects.all()
    }

    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/home.html', context)


# List of all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #  Default url: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


# Detail of a post
class PostDetailView(DetailView):
    model = Post


# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Set author of post to be current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Set author of post to be current login user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check user before updating post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    # Set success url to the home page
    success_url = '/'

    # Check user before deleting post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# About page
def about(request):
    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/about.html', {'title': 'About'})
