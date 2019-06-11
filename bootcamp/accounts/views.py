from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView

from .forms import SignUpForm
from . import forms
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()

            # user.save()
            #
            # profile = profile_form.save(commit=False)
            # profile.user = user
            #
            #
            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            #
            # profile.save()


            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('test')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form,}
                                                            )



