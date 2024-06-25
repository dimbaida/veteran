from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    mobile = forms.CharField(max_length=20, required=True)
    plot = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'mobile', 'plot', 'password1', 'password2')
