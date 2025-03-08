from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password:
            if len(password) < 8:
                self.add_error('password', 'Password is too short (must be at least 8 characters).')
            if password != confirm_password:
                self.add_error('confirm_password', 'Passwords do not match.')

        return cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
