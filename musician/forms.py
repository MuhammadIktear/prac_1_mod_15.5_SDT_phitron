from django import forms
from .models import Musician
class musicianForm(forms.ModelForm):
    class Meta:
        model=Musician
        fields='__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }