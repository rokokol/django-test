from django import forms
from django.contrib.auth import get_user_model

from web.models import NoteSlots

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'new-password'
        })
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password',
            'autocomplete': 'new-password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password is not None:
            if len(password) < 8:
                self.add_error('password', 'Password must be at least 8 characters long.')
            if password != confirm_password:
                self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')


class AuthForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'autocomplete': 'off'
        })
    )


class AddNoteForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your title'
        })
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your note',
            'rows': 12,
        })
    )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title:
            title = title.strip()
        return title

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if text:
            text = text.strip()
        return text

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit=commit)

    class Meta:
        model = NoteSlots
        fields = ('title', 'text')
