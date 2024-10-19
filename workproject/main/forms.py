# accounts/forms.py
from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['number', 'name']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Номер участника'}),
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя участника'}),
        }
