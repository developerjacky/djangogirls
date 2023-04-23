from django.shortcuts import render
from .models import Post

from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })


def helloworld(request):
    x = str(datetime.now())
    return render(request, template_name='helloworld.html')

    # , {'current_time': str(datetime.now()} )  , 'current_time' == 'c'


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})


def hello(request):
    return HttpResponse("Hello")
