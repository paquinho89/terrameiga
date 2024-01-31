
from django.core.exceptions import ValidationError
import random
import re
import os
#Fuction to send the emails to reset the password
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.urls import reverse


#Estas 2 funcions son para cambiarlle o nome a foto da bandeira e que aparezca guay no model do admin con outro nome

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

#Email validation para as newlsetter:
#Eiqui o que se fai é comprobar se o e-mail está na lista negra dos dominios. Básicamente o que trato de facer e que non me metan correos spam
def email_validation(self):
    with open("terrameiga/static/lists/email_black_list.txt", "r") as file_spam_emails:
        #O splitlines é para convertilo a unha lista
        blacklist = file_spam_emails.read().splitlines()
        #Miramos se todo o que está despois do @ está contida na lista negra dos e-mails
        correo_ben=re.search(r"([a-zA-Z0-9äüö_.+-]+$)", self)
        if correo_ben[1] in blacklist:
            raise ValidationError("O teu e-mail é un correo Spam. Por favor, inténteo con outro email")
        elif correo_ben[1]=="":
             raise ValidationError("Este campo non pode estar baleiro")
        else:
            return self
        

#Function to send an email to confirm the email of the new user which just signed up
def send_confirm_email (request, email, username, uidb64, token, language):
    #Con esto o que fago e que o link seax dinámico e colla o 127.0.0.1:8000 cando estamos en local e o terrameiga.bike cando está en production
    current_site = get_current_site(request)
    subject = "TerraMeiga - Email Confirmation"
    # message = f'Click in the following link to confirm your email and create your account http://127.0.0.1:8000/account_confirmation_email_done/{uidb64}/{token}/'
    # IMPORTANTE: As imaxes non se van a renderizar no email porque o dominio (127.0.0.1:8000), é un dominio local. No momento que metas o dominio
    # as imaxes deberíanse renderizar no email que lle chega ao user porque é un dominio seguro é hotmail/gmail/apple non o bloquea. Terás que cambiar a url no
    # arquivo de helpers.px
    message = render_to_string('email_body_confirmation.html', {
        'confirmation_link': f'http://{current_site}/account_confirmation_email_done/{uidb64}/{token}/',
        'visualization_email_link' : f'http://{current_site}' + reverse('email_visualization_url') + f'?username={username}&email={email}&uidb64_url={uidb64}&token_url={token}&language_url={language}',
        'name':username,
    })
    print(f'http://{current_site}' + reverse('email_visualization_url') + f'?username={username}')
    #Se escribo o sender_mail así, o que fago e que aparezca o nome de "TerraMeiga" e así non aparece a dirección de email cando se recibe a mensaxe.
    sender_email = "TerraMeiga <" + settings.EMAIL_HOST_USER + ">"
    recipient_list = [email]
    # Send the email with HTML content
    send_mail(subject, '', sender_email, recipient_list, html_message=message)
    return True

# Function to send the email to reset the password in case it has been forgotten.
def send_reset_password_mail (request, email, uidb64,  token, language):
    #Con esto o que fago e que o link seax dinámico e colla o 127.0.0.1:8000 cando estamos en local e o terrameiga.bike cando está en production
    current_site = get_current_site(request)
    subject = "TerraMeiga - Password Recovery"
    #message = f'Please, click on the link to reset your password http://127.0.0.1:8000/reset_password/{uidb64}/{token}/'
    message = render_to_string('email_body_password.html', {
        'password_recovery_link': f'http://{current_site}/{language}/password_recovery_update/{uidb64}/{token}/',
        #Pasamos a info necesaria a través da url para crear o link NO HTML que se visualiza cando se preme en (In case the email is not correctly displayed...) que me permita o reseteo da password.
        'visualization_email_password_link' : f'http://{current_site}' + reverse('email_visualization_password_recovery_view') + f'?email={email}&uidb64_url={uidb64}&token_url={token}&language_url={language}',
    })
    #Se escribo o sender_mail así, o que fago e que aparezca o nome de "TerraMeiga" e así non aparece a dirección de email cando se recibe a mensaxe.
    sender_email = "TerraMeiga <" + settings.EMAIL_HOST_USER + ">"
    recipient_list = [email]
    # Send the email with HTML content
    send_mail(subject, '', sender_email, recipient_list, html_message=message)
    return True



