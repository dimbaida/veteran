from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('measurement_list')  # Redirect to home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
