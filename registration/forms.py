from django import forms
from .models import rider

class registration_form(forms.ModelForm):
    model = rider
    fields = ('name', 'surname_1', 'surname_2', 'telephone', 'country', 'email')
