from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol
from django.http import Http404

# Create your views here.

def index(request):
    jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'jss':jss})

def detail(request, post_id):
    try:
        my_jss = Jasoseol.objects.get(pk=post_id)
    except:
        raise Http404
    return render(request, 'detail.html', {'my_jss':my_jss})

def create(request):
    if request.method == 'POST':
        filled_form = JssForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    else:
        jss_form = JssForm()
        return render(request, 'create.html', {'jss_form':jss_form})

def update(request, post_id):
    my_jss = Jasoseol.objects.get(pk=post_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == 'POST':
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request, 'create.html', {'jss_form':jss_form})

def delete(request, post_id):
    my_jss = Jasoseol.objects.get(pk=post_id)
    my_jss.delete()
    return redirect('index')