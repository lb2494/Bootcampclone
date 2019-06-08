from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    url = forms.URLField()
    bio = forms.CharField(widget=forms.Textarea({'cols': '20', 'rows': '5'}))
    class Meta:
        model = Profile
        fields = ('bio','url')