from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class userLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', min_length=8, max_length=150)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)



class registerUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', min_length=8, max_length=150)
    email = forms.EmailField(label='Электронная почта')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

