from django import forms
from .models import rider_model

class registration_form_1(forms.ModelForm):
    class Meta:
        model = rider_model
        fields = ('email', 'password', 'password_repetition')
            
        widgets = {
            'email' : forms.EmailInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "pepa@gmail.com"'}),
            'password' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "8 caracteres con maiusculas e caracteres especiais"'}),
            'password_repetition' : forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "8 caracteres con maiusculas e caracteres especiais"'})
        }

# class registration_form_2(forms.ModelForm):
#     class Meta:
#         model = rider_model
#         fields = ('name', 'surname', 'birth_date', 'country', 'region', 'telephone', 'photo')
            
#         widgets = {
#             'name' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "Brasinda"'}),
#             'surname' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "Barreira"'}),
#             'birth_date': forms.DateInput (attrs= {'class': 'form-control'}),
#             'country': forms.Select (attrs = {'class': 'form-control'}),
#             'region': forms.Select (attrs = {'class': 'form-control'}),
#             'telephone' : forms.TextInput (attrs = {'class': 'form-control', 'placeholder':'Ex: "666777888"'})
#             #Para a o campo field de momento non defino o seu widget
#         }

# class registration_form_3(forms.ModelForm):
#     class Meta:
#         model = rider_model
#         fields = ('bicycle_brand', 'bicycle_model', 'navigation_system')
            
#         widgets = {
#             'bicycle_brand' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "Boombtrack"'}),
#             'bicycle_model' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "EXTC"'}),
#             'navigation_system': forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Ex: "EXTC"'})
#         }