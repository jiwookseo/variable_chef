from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthenticationForm(request, form.instance)
            return redirect('accounts:login', form)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('store:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'store:index')
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/form.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/form.html', {'form': form})


@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('store:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/form.html', {'form': form})
