from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView

from .forms import SignUpForm, ProfileForm
from . import forms
# Create your views here.


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()


            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('test')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form,
                                                    'profile_form':profile_form})



