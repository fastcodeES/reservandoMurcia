from django import forms
from .models import *

class RespuestasForm(forms.ModelForm):

    class Meta:
        model = Respuestas
        fields = ['asunto', 'mensaje']
        
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

