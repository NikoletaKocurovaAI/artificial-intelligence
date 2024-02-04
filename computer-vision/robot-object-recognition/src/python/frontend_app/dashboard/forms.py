from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class RegisterRobotForm(forms.Form):
    name = forms.CharField(max_length=128)
    motor_type = forms.CharField(max_length=128)

    # TODO
    # class Meta:
    #     model = Robot
    #     fields = ('name', 'motor_type')


class RobotDetailForm(forms.Form):
    datetime_field = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )
