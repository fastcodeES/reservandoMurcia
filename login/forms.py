from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields
from django.shortcuts import render

class registro_usuarios(UserCreationForm):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)
        
    class Meta:

        model= User
        fields = ['username','email', 'password1', 'password2']