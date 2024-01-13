from django.db import models
import re
from .helpers import email_validation, upload_image_path

#It is a baseline model to modify some fields of the User model which is already created by Django.
# I just want to make the email the unique value.
from django.contrib.auth.models import AbstractUser
from bicicleteiros.static.lists.country_list import country_list_values
#Paquete para traducir texto que se xenera nas view. Neste caso é o texto das alertas
from django.utils.translation import gettext_lazy as _

language_choices = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('gl', _('Galician')),
    ('ca', _('Catalan')),
    ('eu', _('Basque')),
    )

# Create your models here.
#I am creating this model from the AbstractUser model as I just want to make the email the unique identifier
class CustomUser(AbstractUser):
    username = models.CharField(blank=False, null=False, max_length=75, unique=False)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=33, blank=True, null=True)
    language = models.CharField(max_length=33, blank=True, null=True, choices=language_choices)
    
    #This sets the field that will act as a unique identifier of the User model. We are setting it to the email field.
    USERNAME_FIELD = 'email'
    #This sets any other required field for the User model.
    REQUIRED_FIELDS = ['username']

    


    



