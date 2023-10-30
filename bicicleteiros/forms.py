from django import forms
from django.forms import ModelForm
from bicicleteiros.models import chat_comments_model, chat_comments_replies_model


class chat_form(forms.ModelForm):
    class Meta:
        model=chat_comments_model
        fields = ['comentario']
#Esto dos widgets é para meter o formato de bootstrap no form. {{ form }} que está en artigos_content.html.
#O attrs é CSS style
        widgets = {
            'comentario': forms.Textarea (attrs = {'class': 'form-control', 'style': "background-color: black; color:white", 'placeholder':'Write your text here',
                                                    'rows':1})
        }



#Form for the replies
class chat_replies_form(forms.ModelForm):
    class Meta:
        model=chat_comments_replies_model
        fields = ['reply_text', 'pk_original_comment']
#Esto dos widgets é para meter o formato de bootstrap no form. {{ form }} que está en artigos_content.html.
#O attrs é CSS style
        widgets = {
            'reply_text': forms.Textarea (attrs = {'class': 'form-control', 'style': "background-color: #28231D; color:white", 'placeholder':'Write here your reply',
                                                    'rows':1}),
            'pk_original_comment': forms.Textarea()
        }