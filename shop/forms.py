from .models import Customer
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'placeholder': 'username'
            }),

            "password": TextInput(attrs={
                'placeholder': 'password'
            }),

        }
