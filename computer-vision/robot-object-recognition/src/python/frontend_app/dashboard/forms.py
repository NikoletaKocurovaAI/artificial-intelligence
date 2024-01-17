from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import TextField, CharField

from .models import Robot


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RegisterRobotForm(forms.Form):
    name = forms.CharField()
    motor_type = forms.CharField()
    #name = TextField(null=False, blank=False)
    #motor_type = TextField(null=False, blank=False)

    # class Meta:
    #     model = Robot
    #     fields = ("name", "motor_type")