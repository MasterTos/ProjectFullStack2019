from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def auth_page(request):
    return render(request, 'example_app/auth_page.html')

def home(request):
    context = dict()

    if request.user.is_authenticated:
        context['greeting'] = 'Welcome Back {}'.format(request.user)
    else:
        context['greeting'] = 'Welcome Anonymous'

    return render(request, 'example_app/home.html', context)

@login_required
def logoutView(request):
    logout(request)
    return redirect('home')