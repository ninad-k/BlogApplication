from django.shortcuts import render

posts = [
    {
        'author': 'NinadK',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 18, 2020',
    },
    {
        'author': 'PallaviK',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'April 18, 2020',
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
