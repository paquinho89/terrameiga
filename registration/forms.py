from django import forms
#from .models import sign_in_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
#Este é un modelo que xa está preconfigurado por django e chámase user. Ten campos definidos como username, email, password...
from django.contrib.auth.models import User
from .models import CustomUser
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
#ESto son paquetes para traducir os textos. Eiqui o que quero traducir é o placeholder do formulario
from django.utils.translation import gettext_lazy as _

class sign_in_form_1(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
            
        widgets = {
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
            'password' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'min 8 caracteres'}),
        }

class sign_up_form_2(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
            
        widgets = {
            'username' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Brasinda'}),
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
            'password1' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
            'password2' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
        }

class personal_data_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'country', 'language')
            
        widgets = {
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
            'username' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'username'}),
            'country' : forms.Select(attrs = {'class': 'form-control'}),
            'language' : forms.TextInput(attrs = {'class': 'form-control'}),
        }
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class password_update_form(PasswordChangeForm):
    class Meta:
        model = CustomUser
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class delete_account_form(forms.Form):
    text_to_delete = forms.CharField(label="terrameiga", max_length=100, widget=forms.TextInput(attrs={
                                                                                                        'class': 'form-control', 
                                                                                                        'placeholder': _('type "terrameiga". Lowercase and without quotes')}))
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class password_reset_form(PasswordResetForm):
    class Meta:
        model = CustomUser
        fields = ('email')
            
        widgets = {
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
        }
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class password_new_form(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ('new_password1', 'new_password2')
            
        widgets = {
            'new_password1' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'new_password1'}),
            'new_password2' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'new_password2'}),
        }
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())





        





