from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Create your views here.

def signup(request):
    if request.method == 'POST':
        filled_form = UserCreationForm(request.POST)
        print(filled_form.is_valid())
        if filled_form.is_valid():
            filled_form.save()
            return redirect('index')
    regi_form = UserCreationForm()
    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView):
    template_name = 'login.html'