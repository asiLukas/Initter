from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_pic',
            'description'

        ]
