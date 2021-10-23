from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Create custom form inheriting from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # New field: Email
    email = forms.EmailField()

    # Configure form
    class Meta:
        # Model will be affected after calling form.save() -> User
        model = User
        # Fields show in the form in order
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # New field: Email
    email = forms.EmailField()

    # Configure form
    class Meta:
        # Model will be affected after calling form.save() -> User
        model = User
        # Fields show in the form in order
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']