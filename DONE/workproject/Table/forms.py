from django import forms

class ParticipantSearchForm(forms.Form):
    number = forms.IntegerField(label='Номер участника', required=True)
