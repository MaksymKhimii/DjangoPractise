from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'placeholder': 'username'
            }),

            "password": TextInput(attrs={
                'placeholder': 'password'
            }),

        }
