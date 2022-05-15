from django import forms
from .models import *
from django.views import generic


class TareasForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = '__all__'