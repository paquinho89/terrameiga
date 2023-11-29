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


#FAGO ESTO PORQUE TANTO O AuthenticationFor   E O UserCreatioForm son formularios que xa está predefinidos en Django e eu quer sobrescribir as súas clases.

class CustomAuthenticationFormSignIn(AuthenticationForm):
    #Con esto o que fago e resetear a clase que ten o AuthenticationForm e asignarmee a clase de bootstrap conocida como "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for Bootstrap styling form-control
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

class sign_in_form_1(CustomAuthenticationFormSignIn):
    class Meta:
        model = CustomUser


class CustomAuthenticationFormSignUp(UserCreationForm):
    #Con esto o que fago e resetear a clase que ten o AuthenticationForm e asignarmee a clase de bootstrap conocida como "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for Bootstrap styling form-control
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'width': '30px', 'height': '20px'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
                    

class sign_up_form_2(CustomAuthenticationFormSignUp):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
            
        

class personal_data_form(forms.ModelForm):
    def __init__(self, *args, sorted_country_list=None, **kwargs):
        #Con esto inicio os argumentos da clase pai/mai que é forms.ModelForm
        super().__init__(*args, **kwargs)
        # Populate choices for 'country' field dynamically
        self.fields['country'].widget.choices = sorted_country_list
        
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'country', 'language')
            
        widgets = {
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'brasinda@gmail.com'}),
            'username' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'username'}),
            'country' : forms.Select(attrs = {'class': 'form-control'}),
            'language' : forms.Select(attrs = {'class': 'form-control'}),
        }
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

class CustomAuthenticationFormPasswordChangeForm (PasswordChangeForm):
    #Con esto o que fago e resetear a clase que ten o AuthenticationForm e asignarmee a clase de bootstrap conocida como "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for Bootstrap styling form-control
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


class password_update_form(CustomAuthenticationFormPasswordChangeForm):
    class Meta:
        model = CustomUser
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class delete_account_form(forms.Form):
    text_to_delete = forms.CharField(label="terrameiga", max_length=100, widget=forms.TextInput(attrs={
                                                                                                        'class': 'form-control', 
                                                                                                        'placeholder': _('type "terrameiga". Lowercase and without quotes')}))
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class CustomAuthenticationFormPasswordReset(PasswordResetForm):
    #Con esto o que fago e resetear a clase que ten o AuthenticationForm e asignarmee a clase de bootstrap conocida como "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for Bootstrap styling form-control
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class password_reset_form(CustomAuthenticationFormPasswordReset):
    class Meta:
        model = CustomUser


class CustomAuthenticationFormNewPassword (SetPasswordForm):
    #Con esto o que fago e resetear a clase que ten o AuthenticationForm e asignarmee a clase de bootstrap conocida como "form-control"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update widget attributes for Bootstrap styling form-control
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

class password_new_form(CustomAuthenticationFormNewPassword):
    class Meta:
        model = CustomUser
        fields = ('new_password1', 'new_password2')
            
        widgets = {
            'new_password1' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'new_password1'}),
            'new_password2' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'new_password2'}),
        }
        #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())





        





