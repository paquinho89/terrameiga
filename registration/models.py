from django.db import models
import re
from .helpers import email_validation, upload_image_path

#It is a baseline model to modify some fields of the User model which is already created by Django.
# I just want to make the email the unique value.
from django.contrib.auth.models import AbstractUser
from bicicleteiros.static.lists.country_list import country_list_values
#Con esto obteño o language que está identificando a función de django.middleware.locale.LocaleMiddleware (é un paquete que está no settings)
from django.utils.translation import get_language

#REGION LIST
#Esta función e para traer todos os regions que están nos .txt
#Teño que crear unha tupla porque é o que lle hai que pasar o dropdown
with open("terrameiga/static/lists/languages.txt", "r") as language_list_file:
    language_list = tuple(language_list_file)
    language_list_fixed = tuple(([re.search('[^\n]*',language)[0],re.search('[^\n]*',language)[0]]) for language in language_list)

language_choices = (
    ('en', 'en'),
    ('es', 'es'))

# Create your models here.
#I am creating this model from the AbstractUser model as I just want to make the email the unique identifier
class CustomUser(AbstractUser):
    username = models.CharField(blank=False, null=False, max_length=75, unique=False)
    email = models.EmailField(unique=True)
    #country = models.CharField(max_length=33, choices= country_list_values, blank=True, null=True)
    country = models.CharField(max_length=33, choices= country_list_values, blank=True, null=True)
    language = models.CharField(max_length=33, blank=True, null=True, choices=language_choices)
    
    #This sets the field that will act as a unique identifier of the User model. We are setting it to the email field.
    USERNAME_FIELD = 'email'
    #This sets any other required field for the User model.
    REQUIRED_FIELDS = ['username']


    



