from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm, CustomPasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect(reverse('electricity:measurements'))  # Redirect to home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('electricity:measurements'))  # Redirect to some view after successful login
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('authuser:password_change_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})
