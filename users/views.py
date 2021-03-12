from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            form.save()
            messages.success(
                request, f'User {user_name} is succesfully registered')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Registration',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'title': f'Profile-{request.user.username}',
        'form': form

    }

    return render(request, 'users/profile.html', context)
