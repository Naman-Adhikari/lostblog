from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200, label="Nickname")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']
