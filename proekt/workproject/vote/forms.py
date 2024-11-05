from django import forms
from .models import Score
from main.models import Participant  # Импортируем участников

class ScoreForm(forms.ModelForm):
    participant = forms.ModelChoiceField(queryset=Participant.objects.all(), label="Участник")

    class Meta:
        model = Score
        fields = ['participant', 'technique', 'composition', 'creativity', 'impression']
        labels = {
            'technique': 'Техника',
            'composition': 'Композиция',
            'creativity': 'Креативность',
            'impression': 'Впечатление',
        }
        widgets = {
            'technique': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'composition': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'creativity': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'impression': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }
