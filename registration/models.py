from django.db import models
import os
import random
import re
from django.core.exceptions import ValidationError

#Estas 2 funcions son para cambiarlle o nome a foto do corredor e que aparezca guay no model do admin con outro nome

def get_filename_extension (filepath):
    #Esto colle a parte final da ruta, que será algo como "C/Users/Desktop/hat.png"
    #Pois o os.path.basename o que está facendo e colloer solo o "hat.png"
    base_name=os.path.basename(filepath)
    #Esto dividi o "hat.png" en hat (que será o name) e na ext (extensión), que será "png"
    name, ext =os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    #This is given a random number as a name to the picture uploaded for the file
    new_filename=random.randint(1,999)
    name, ext= get_filename_extension(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "media_files/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


#Email validation:
#Eiqui o que se fai é comprobar se o e-mail está na lista negra dos dominios. Básicamente o que trato de facer e que non me metan correos spam
def email_validation(self):
    with open("terrameiga/static/email_black_list.txt", "r") as file_spam_emails:
        #O splitlines é para convertilo a unha lista
        blacklist = file_spam_emails.read().splitlines()
        #Miramos se todo o que está despois do @ está contida na lista negra dos e-mails
        correo_ben=re.search(r"([a-zA-Z0-9äüö_.+-]+$)", self)
        if correo_ben[1] in blacklist:
            raise ValidationError("O teu e-mail é un correo Spam. Por favor, inténteo con outro email")
        else:
             return self


# Create your models here.
class rider (models.Model):
    name = models.CharField(blank=False, null=False, max_length=75)
    surname_1 = models.CharField(blank=False, null=False, max_length=75)
    surname_2 = models.CharField(blank=False, null=False, max_length=75)
    telephone = 
    photo = models.ImageField(upload_to=upload_image_path, null=True, blank = True)
    nationality = models.CharField(max_length=11, choices=evento_choices)
    languages = models.CharField(max_length=11, choices=evento_choices)
    country = models.CharField(max_length=11, choices=evento_choices)
    region = models.CharField(max_length=11, choices=evento_choices)
    email = models.EmailField(blank=False, max_length=255, validators=[email_validation])
    password =
    password_repetition =

    bicycle_brand = models.CharField(blank=False, null=False, max_length=75)
    bicycle_model = models.CharField(blank=False, null=False, max_length=75)
    wheel_dyameter = models.DecimalField(max_digits=5, decimal_places=2)
    tyre_thickness = models.DecimalField(max_digits=5, decimal_places=2)
    navigation_system = models.CharField(blank=False, null=False, max_length=75)
