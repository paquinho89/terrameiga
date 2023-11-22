from django import forms
from django.forms import ModelForm
from bicicleteiros.models import chat_comments_replies_model
#ESto son paquetes para traducir os textos. Eiqui o que quero traducir é o placeholder do formulario
from django.utils.translation import gettext_lazy as _


#Form for the replies
class chat_replies_form(forms.ModelForm):
    class Meta:
        model=chat_comments_replies_model
        fields = ['reply_text', 'pk_original_comment']
#Esto dos widgets é para meter o formato de bootstrap no form. {{ form }} que está en artigos_content.html.
#O attrs é CSS style
        widgets = {
            'reply_text': forms.Textarea (attrs = {'class': 'form-control', 
                                                   'style': "background-color: #28282B; color:white", 
                                                   'placeholder': _('Write here your reply'),
                                                    'rows':1}),
            'pk_original_comment': forms.Textarea()
        }