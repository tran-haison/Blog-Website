from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'October 19th, 2021',
#     },
#     {
#         'author': 'Hai Son',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'November 20th, 2032',
#     },
# ]

def home(request):
    # Dummy data needs to be passed
    context = {
        'posts': Post.objects.all()
    }

    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/home.html', context)


def about(request):
    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/about.html', {'title': 'About'})
