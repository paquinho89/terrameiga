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

#Estas son as distintas opcións que se presentan para seleccionar o avatar da bicicleta:
avatar_bike_choices = (
    ('commuter_bike','/static/pictures/bike_avatars/commuter_bike.png'),
    ('electrical_bike', '/static/pictures/bike_avatars/electrical_bike.jpg'),
    ('folding_bike', '/static/pictures/bike_avatars/folding_bike.jpg'),
    ('kid_bike', '/static/pictures/bike_avatars/kid_bike.jpg'),
    ('mountain_bike', '/static/pictures/bike_avatars/mountain_bike.jpg'),
    ('old_bike', '/static/pictures/bike_avatars/old_bike.jpg'),
    ('road_bike', '/static/pictures/bike_avatars/road_bike.jpg'),
    ('touring_bike', '/static/pictures/bike_avatars/touring_bike.jpg'),
)

# Create your models here.
#I am creating this model from the AbstractUser model as I just want to make the email the unique identifier
class CustomUser(AbstractUser):
    username = models.CharField(blank=False, null=False, max_length=75, unique=False)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    language = models.CharField(max_length=33, choices= language_list_fixed, blank=True, null=True)
    profile_bike = models.CharField(max_length=33, choices= avatar_bike_choices, blank=True, null=True, unique=True)
    
    #This sets the field that will act as a unique identifier of the User model. We are setting it to the email field.
    USERNAME_FIELD = 'email'
    #This sets any other required field for the User model.
    REQUIRED_FIELDS = ['username']



