from django.db import models
import re
from datetime import datetime
from django.utils import timezone
from registration.models import CustomUser
import random, os
from bicicleteiros.static.lists.country_list import country_list_values
#ESto utilízoo para traducir os países da lista. Temos que por o _lazy porque estamos a traballar con modelos.
from django.utils.translation import gettext_lazy as _
#PAra o rich text do text field dos artigos no django/admin
from ckeditor.fields import RichTextField
from bicicleteiros.static.lists.currency_list import currency_list_values

with open("bicicleteiros/static/lists/time_zone_list.txt", "r") as time_zone_list_file:
    time_zone_list = tuple(time_zone_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    time_zone_list_fixed = tuple(([re.search('[^\n]*',time_zone)[0],re.search('[^\n]*',time_zone)[0]]) for time_zone in time_zone_list)

# Create your models here.
day_type_choices = (
    ('resting', 'resting'),
    ('cycling', 'cycling')
)

night_type_choices = (
    ('outside',       'outside'      ),
    ('accommodation', 'accommodation')
)
#---------------------------
expense_type_choices = (
    ( 'supermarket',     'supermarket'),
    ( 'restaurant',      'restaurant'),
    ( 'accommodation',   'accommodation'),
    ( 'transport',       'transport'),
    ( 'bureaucracy',     'bureaucracy'),
    ( 'other',           'other')
)

#---------------------------
continent_choices = (
    ( 'Europe', 'Europe'),
    ( 'Asia', 'Asia'),
    ( 'Oceania', 'Oceania'),
    ( 'America', 'America'),
    ( 'Africa', 'Africa')
)

#Modelo para os comentarios:
class chat_comments_model(models.Model):
    comentario_en = RichTextField()
    comentario_es = RichTextField()
    comentario_gl = RichTextField()
    #Teño que utilizar DateField e non podo utilizar o DateTimeField porque na base de datos de Postgress
    #de Railway non me acepta o datetime field.
    #date_added = models.DateField (default=datetime.now, blank=True, null=True)
    date_added = models.DateTimeField (default=timezone.now, blank=True, verbose_name='date_autofilled')
    username_comment = models.CharField(max_length=33, blank=True, null=True, default="paquinho89", verbose_name="username_autofilled")
    number_of_replies = models.IntegerField(blank=False, null=True, default=0, verbose_name="number_replies_autofilled")

    #Esto é para que me ordene os comentarios na páxina por data. Os comentarios máis recentes que se posicionen arriba
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return (str(self.pk))
    
#Modelo no que se gardarán as replies dos comentarios
class chat_comments_replies_model(models.Model):
    pk_original_comment = models.ForeignKey(chat_comments_model, on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField(blank=False)
    date_added = models.DateTimeField(default=timezone.now, blank=True)
    username_reply = models.CharField(max_length=33, blank=True, null=True)
    
    #Esto é para que me ordene os replies na páxina por data. Os comentarios máis recentes que se posicionen arriba
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return (str(self.username_reply))


class currency(models.Model):
    currency = models.CharField(max_length=50, choices= currency_list_values, blank=False, null=False)
    currency_change_euro = models.DecimalField(max_digits=15, decimal_places=5, blank = False, null=False)
    
    def __str__(self):
        return (self.currency)

    
class country_information_model(models.Model):
    country = models.CharField(max_length=33, choices= country_list_values, blank=True, null=True, unique=True)
    continent = models.CharField(max_length=33, choices= continent_choices, blank=True, null=True, default="Europe")
    country_number = models.IntegerField(blank=False, null=False)
    capital_town = models.CharField(max_length=33, blank=True, null=True)
    surface = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_density = models.IntegerField(blank=True, null=True)
    life_expectancy = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(currency, on_delete=models.PROTECT)
    time_zone = models.CharField(max_length=33, choices= time_zone_list_fixed, blank=True, null=True)
    visa_requerided = models.CharField(max_length=33, choices= (('yes', 'yes'), ('no','no')), blank=True, null=True)
    visa_price = models.DecimalField(max_digits=15, decimal_places=0, blank = True, null=True, default=0)
    interesting_fact_en = models.CharField(max_length=255, blank=True, null=True)
    interesting_fact_es = models.CharField(max_length=255, blank=True, null=True)
    interesting_fact_gl = models.CharField(max_length=255, blank=True, null=True)
    interesting_fact_eu = models.CharField(max_length=255, blank=True, null=True)
    interesting_fact_ca = models.CharField(max_length=255, blank=True, null=True)
    song_spotify = models.CharField(max_length=255, blank=False, null=False)

    #Esto é para que me ordene os países polo número de país
    class Meta:
        ordering = ['-country_number']

    def __str__(self):
        return (self.country)

#Agora obteño a semana na que estou dependendo da data de inicio
#We get the day of the year
#IMPORTANTE!!!: Eiqui tes que cambiar a data e por a data na que comezas a viaxe.
starting_day_of_year = datetime(2024,3,12).timetuple().tm_yday
current_day_of_year = datetime.now().timetuple().tm_yday
#Sumamos 1 para que o primer día me conte como o day 1
day_in_the_journey = (current_day_of_year - starting_day_of_year)+1
#Suamos 1 para que a primeira semana conte como semana 1 e non como semana 0.
week_day = ((current_day_of_year - starting_day_of_year)/7)+1

class money_model(models.Model):
    journey_day = models.IntegerField(default=int(day_in_the_journey), null=True)
    week = models.IntegerField(default=int(week_day), null=True) 
    country = models.ForeignKey(country_information_model, on_delete=models.PROTECT)
    continent = models.CharField(max_length=33, choices= continent_choices, blank=True, null=True, verbose_name="continent_autofilled")
    country_number = models.IntegerField(blank=True, null=True, verbose_name="country_number_autofilled")
    #Teño que duplicar o country_name porque á hora de tratar os datos, o country como ten un Foreign key móstrame un número no eixe x do gráfico e eu quero que me mostre o
    # nome do daís. E para que me mostre o nome do país o campo ten que ser un "CharField" e non un Foreign Key.
    # De todos os xeitos o "country_name" calcúlase automáticamente xa que colle o mesmo valor que o country.
    country_name = models.CharField(max_length=33, blank=True, null=True, verbose_name="country_name_autofilled")
    expense = models.DecimalField(max_digits=15, decimal_places=2, blank = False, null=False)
    expense_type = models.CharField(max_length=33, choices=expense_type_choices, blank=False, null=False)
    expense_euros = models.IntegerField(blank = True, null=True, verbose_name="expense_euros_autofilled")

    #Convert the money into Euros base on the currency change of the "currency model".
    def save(self):
        self.expense_euros = sum([self.expense*self.country.currency.currency_change_euro])
        self.country_name = str(self.country)
        self.country_number = str(self.country.country_number)
        self.continent = str(self.country.continent)
        return super().save()
    #Esto é para que me ordene as entradas de diñeiro pondo os máis recentes arriba na lista.
    class Meta:
        ordering = ['-journey_day']

    def __str__(self):
        return (str(self.journey_day) + ' days ' + self.expense_type + ' ' + self.country_name)
    
class km_altitude_model (models.Model):
    journey_day = models.IntegerField(default=int(day_in_the_journey), null=True)
    week = models.IntegerField(default=int(week_day), null=True)
    country = models.ForeignKey(country_information_model, on_delete=models.PROTECT)
    continent = models.CharField(max_length=33, choices= continent_choices, blank=True, null=True, verbose_name="continent_autofilled")
    country_number = models.IntegerField(blank=True, null=True, verbose_name="country_number_autofilled")
    #Teño que duplicar o country_name porque á hora de tratar os datos, o country como ten un Foreign key móstrame un número no eixe x do gráfico e eu quero que me mostre o
    # nome do daís. E para que me mostre o nome do país o campo ten que ser un "CharField" e non un Foreign Key.
    # De todos os xeitos o "country_name" calcúlase automáticamente xa que colle o mesmo valor que o country.
    country_name = models.CharField(max_length=33, blank=True, null=True, verbose_name="country_name_autofilled") 
    km_day = models.IntegerField(blank = True, null=True)
    altitude_day = models.IntegerField(blank = True, null=True)
    day_type = models.CharField(max_length=33, choices=day_type_choices, blank=True, null=True)
    night_type = models.CharField(max_length=33, choices=night_type_choices, blank=True, null=True)

    #Convert the money into Euros based on the currency change of the "country_information_model".
    def save(self):
        self.country_name = str(self.country)
        self.country_number = str(self.country.country_number)
        self.continent = str(self.country.continent)
        return super().save()
    
    #Esto é para que me ordene as entradas dos km e ascenso pondo os máis recentes arriba na lista.
    class Meta:
        ordering = ['-journey_day']
    
    def __str__(self):
        return (str(self.journey_day) + ' days ' + self.country_name )

class videos_model (models.Model):
    week = models.IntegerField(default=int(week_day), null=True)
    youtube_link = models.CharField(max_length=1000, null=True, blank = True)
    #Esto é para que me ordene os vídeos pondo os máis recentes arriba na lista.
    class Meta:
        ordering = ['-week']

    def __str__(self):
        return 'Week ' + str(self.week)


def get_filename_extension (filepath):
    #Esto colle a parte final da ruta, que será algo como "C/Users/Desktop/hat.png"
    #Pois o os.path.basename o que está facendo e coller solo o "hat.png"
    base_name=os.path.basename(filepath)
    #Esto dividi o "hat.png" en hat (que será o name) e na ext (extensión), que será "png"
    name, ext =os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    #The **instance** argument refers to the model instance the image is associated with
    #The **filename** argument is the original name of the uploaded file and it has to be like that because the upload_to.
    #I am not using filename, however I have to include it as the "upload_to" APIs function in the "image_file" field of the model expects 2 arguments.
    #This is taking the country the picture is associated with and naming the folder with the country of the picture
    folder_name=instance.country
    #This is given a random number as a name to the picture uploaded for the file
    file_name=random.randint(1,999)
    name, ext= get_filename_extension(str(instance.image_file))
    final_filename='{file_name}{ext}'.format(file_name=file_name, ext=ext)
    return "media_files/{folder_name}/{final_filename}".format(folder_name=folder_name, final_filename=final_filename)


class photos_model (models.Model):
    country = models.ForeignKey(country_information_model, on_delete=models.PROTECT)
    country_number = models.IntegerField(blank=True, null=True, verbose_name="deixar_en_blanco")
    image_file = models.ImageField(upload_to=upload_image_path, null=True, blank = True, verbose_name="TerraMeiga_picture")

    #Esto é para que me ordene os vídeos pondo os máis recentes arriba na lista.
    class Meta:
        ordering = ['-country_number']

    #Auto-completar o country_number automáticamente dependendo do country que se seleccione.
    def save(self):
        self.country_number = str(self.country.country_number)
        return super().save()

    def __str__(self):
        return str(self.country) + ' ' + str(self.image_file)  




