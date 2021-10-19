from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 19th, 2021',
    },
    {
        'author': 'Hai Son',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 20th, 2032',
    },
]


def home(request):
    # Data needs to be passed
    context = {
        'posts': posts
    }

    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/home.html', context)


def about(request):
    # Return a http response
    # Specify a relative path from "templates" folder
    return render(request, 'blog/about.html', {'title': 'About'})
