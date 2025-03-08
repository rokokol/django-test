from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from web.forms import RegistrationForm


def main_view(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
