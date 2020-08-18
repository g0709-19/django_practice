from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def create(request):
    if request.method == 'POST':
        post = Post()
        post.profile = request.POST['profile']
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'create.html', {'form':form})

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')