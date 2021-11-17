from django.shortcuts import render
from django.shortcuts import HttpResponse

posts = [
    {
        'author': 'MugdhaS',
        'title': 'BlogPost 1',
        'Content': 'First post content',
        'date_posted': 'Nov, 11 2021'
    },
    
    {
        'author': 'John Doe',
        'title': 'BlogPost 2',
        'Content': 'Second post content',
        'date_posted': 'Nov, 11 2021'
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