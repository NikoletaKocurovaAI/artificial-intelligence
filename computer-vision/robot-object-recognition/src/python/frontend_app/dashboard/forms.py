from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form): # TODO from django.views.generic import FormView
    username = forms.CharField()
    password = forms.CharField()


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RegisterRobotForm(forms.Form):
    name = forms.CharField() # TODO models.py 128 chars
    motor_type = forms.CharField()

    # TODO Difference?
    # class Meta:
    #     model = Robot
    #     fields = ("name", "motor_type")

    # TODO validate if robot name already exists