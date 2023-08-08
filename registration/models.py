from django.db import models
import re
from .helpers import email_validation, upload_image_path

#It is a baseline model to modify some fields of the User model which is already created by Django.
# I just want to make the email the unique value.
from django.contrib.auth.models import AbstractUser


#COUNTRY LIST
#Esta función e para traer todos os countries que están nos .txt
#Teño que crear unha tupla porque é o que lle hai que pasar o dropdown
with open("terrameiga/static/lists/country_list_en.txt", "r") as country_list_file:
    country_list = tuple(country_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    country_list_fixed = tuple(([re.search('[^\n]*',country)[0],re.search('[^\n]*',country)[0]]) for country in country_list)

#REGION LIST
#Esta función e para traer todos os regions que están nos .txt
#Teño que crear unha tupla porque é o que lle hai que pasar o dropdown
with open("terrameiga/static/lists/languages.txt", "r") as language_list_file:
    language_list = tuple(language_list_file)
    language_list_fixed = tuple(([re.search('[^\n]*',language)[0],re.search('[^\n]*',language)[0]]) for language in language_list)

# Create your models here.
#I am creating this model from the AbstractUser model as I just want to make the email the unique identifier
class CustomUser(AbstractUser):
    username = models.CharField(blank=False, null=False, max_length=75, unique=False)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    language = models.CharField(max_length=33, choices= language_list_fixed, blank=True, null=True)
    
    #This sets the field that will act as a unique identifier of the User model. We are setting it to the email field.
    USERNAME_FIELD = 'email'
    #This sets any other required field for the User model.
    REQUIRED_FIELDS = ['username']



# class sign_in_model (models.Model):
#     email = models.EmailField(blank=False, null=False, max_length=255, validators=[email_validation])
#     password = models.CharField(blank=False, null=False, max_length=255)
#     password_repetition = models.CharField(blank=False, null=False, max_length=255)
    #name = models.CharField(blank=False, null=False, max_length=75)
    #surname = models.CharField(blank=False, null=False, max_length=75)
    #birth_date = models.DateField (blank=False)
    #country = models.CharField(max_length=33, choices = country_list)
    ##region = models.CharField(max_length=20, choices=region_list)
        
    #country_telephone_code =
    #telephone = models.IntegerField(blank=False, null=False)
    #O null=True é para que acepte valores en blanco no data base e o blank=True é para que o valor non sexa requerido por Django, desta forma non fai falta que exista unha imaxe
    #photo = models.ImageField(upload_to=upload_image_path, null=True, blank = True)
    
    #bicycle_brand = models.CharField(blank=False, null=False, max_length=75)
    #bicycle_model = models.CharField(blank=False, null=False, max_length=75)
    #navigation_system = models.CharField(blank=False, null=False, max_length=75)
