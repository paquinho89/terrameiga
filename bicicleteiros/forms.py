from django import forms
from django.forms import ModelForm
from bicicleteiros.models import chat_comments


class chat_form(forms.ModelForm):
    class Meta:
        model=chat_comments
        fields = ['comentario']
#Esto dos widgets é para meter o formato de bootstrap no form. {{ form }} que está en artigos_content.html.
#O attrs é CSS style
        widgets = {
            'comentario': forms.Textarea (attrs = {'class': 'form-control'})
        }