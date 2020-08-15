from django.shortcuts import render, redirect
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'jss':all_jss})

@login_required(login_url='/login/')
def my_index(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'jss':my_jss})

def detail(request, post_id):
    try:
        my_jss = Jasoseol.objects.get(pk=post_id)
    except:
        raise Http404
    comment_form = CommentForm()
    return render(request, 'detail.html', {'my_jss':my_jss, 'comment_form':comment_form})

@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author = request.user
            temp_form.save()
            # 오브젝트가 생성, 업데이트가 되기 전에
            # 저장을 지연시키고 그 사이에 어떤 것을 해줄 수가 있다.
            filled_form.save()
            return redirect('index')
    else:
        jss_form = JssForm()
        return render(request, 'create.html', {'jss_form':jss_form})

def update(request, post_id):
    my_jss = Jasoseol.objects.get(pk=post_id)
    if request.user != my_jss.author:
        raise PermissionDenied
    if request.method == 'POST':
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    jss_form = JssForm(instance=my_jss)
    return render(request, 'create.html', {'jss_form':jss_form})

def delete(request, post_id):
    my_jss = Jasoseol.objects.get(pk=post_id)
    if request.user == my_jss.author:
        my_jss.delete()
        return redirect('index')

    raise PermissionDenied

def create_comment(request, jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail', jss_id)

def delete_comment(request, jss_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)
    else:
        raise PermissionDenied