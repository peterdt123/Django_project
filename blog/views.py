from django.shortcuts import render

posts = [
    {
        'author' : 'Peter Tran',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'March 19, 2019'
    },
    {
        'author' : 'Jane Paeng',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'March 20, 2019'
    }    
]


# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 