from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import TextField, CharField

from .models import Robot


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65)


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        # TODO define users name max length to 65 chars
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput(),
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput()
        }

class RegisterRobotForm(forms.Form):
    name = TextField(null=False, blank=False)
    motor_type = TextField(null=False, blank=False)

    class Meta:
        model = Robot
        fields = ("name", "motor_type")