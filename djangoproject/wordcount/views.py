from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    count = {}
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    return render(request, "result.html", {'full':text, 'total':len(words), 'count':count.items()})