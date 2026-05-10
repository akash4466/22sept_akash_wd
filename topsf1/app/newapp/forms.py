from django import forms
from .models import *

class Studform(forms.ModelForm):
    class Meta:
        model=stud
        fields='__all__'
