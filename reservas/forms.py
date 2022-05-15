from collections import UserString
from django import forms
from .models import *
from django.views import generic


class ReservasForm(forms.ModelForm):

    

    class Meta:
        model = Reserva
        fields = ['nombre', 'email', 'numero_asistentes', 'horario', 'telefono', 'fecha_reserva', 'username']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'class':'datepicker', 'readonly':'readonly'}),
            'username': forms.TextInput(attrs={'class':'invisible', 'value':'none'}),
        }

        fecha_reserva = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y/')
        )