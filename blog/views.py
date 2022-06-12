from django.shortcuts import render
# from django.http import HttpResponse

posta = [
    {
        'author': 'Jaskaran Singh',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '12 June 2022'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '20 June 2022'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posta
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

