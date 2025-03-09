from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, AddNoteForm
from web.models import NoteSlots


def index_view(request):
    form = AuthForm()
    notes = NoteSlots.objects.order_by('?')[:10]

    return render(request, 'web/index.html',
                  {
                      'form': form,
                      'notes': notes
                  })


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


def note_add_view(request):
    form = AddNoteForm()
    if request.method == 'POST':
        form = AddNoteForm(data=request.POST, initial={'user': request.user})
        if form.is_valid():
            note = form.save(commit=True)
            print(f'note {note} is saved successfully')
            return redirect('index')

    return render(request, 'web/note_add_form.html', {'form': form})


def note_edit_view(request, note_id):
    is_real_id = NoteSlots.objects.filter(id=note_id).exists()
    note = None
    if is_real_id:
        note = NoteSlots.objects.get(id=note_id)
    if (id is None or
          note is None or
          not is_real_id):
        return note_add_view(request)
    else:
        if not request.user.is_authenticated or note.user.id != request.user.id:
            print(1)
        else:
            print(2)
        return note_add_view(request)
