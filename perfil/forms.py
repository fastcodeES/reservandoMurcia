from django import forms
from .models import *
from django.views import generic
from django.contrib.auth.models import User


class ChangePasswordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['password']
        widgets = {
            'password': forms.PasswordInput(),
            }

class ChangeEmailForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']