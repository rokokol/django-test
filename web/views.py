from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm


def index_view(request):
    form = AuthForm()
    return render(request, 'web/index.html', {'form': form})


def registration_view(request):
    form = RegistrationForm()
    is_registered = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()

            is_registered = True
            print(form.cleaned_data)
    return render(request, 'web/registration_form.html',
                  {
                      'form': form,
                      'is_registered': is_registered
                  })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Email or password is incorrect')
            else:
                login(request, user)
                return redirect('index')
    return render(request, 'web/auth_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
