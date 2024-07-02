from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=255, required=True)
    lastname = forms.CharField(max_length=255, required=True)
    mobile = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'mobile', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomPasswordChangeForm(PasswordChangeForm):
    # Add custom fields or customization here
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing form fields, for example:
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'})
