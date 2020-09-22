from django import forms
from mpttapp.models import Mydata


class Folderform(forms.Form):
    body = forms.CharField(max_length=140)
    title = forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)