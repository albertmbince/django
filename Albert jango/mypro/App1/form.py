from django import forms
from .models import*
class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'