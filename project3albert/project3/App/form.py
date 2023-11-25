from django import forms
from App.models import*

class studentform(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'