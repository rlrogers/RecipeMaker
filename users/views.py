from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Great, your account has been created! You're now able to log into the home page.")
            return redirect( 'login' )          
    else:
        form = UserRegisterForm()
    # Double check context dict bellow
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context) 