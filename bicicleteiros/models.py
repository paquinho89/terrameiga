from django.db import models
import re
from datetime import datetime
from django.utils import timezone
from registration.models import CustomUser
import random, os


with open("bicicleteiros/static/lists/country_list.txt", "r") as country_list_file:
    country_list = tuple(country_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    country_list_fixed = tuple(([re.search('[^\n]*',country)[0],re.search('[^\n]*',country)[0]]) for country in country_list)

with open("bicicleteiros/static/lists/currency_list.txt", "r") as currency_list_file:
    currency_list = tuple(currency_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    currency_list_fixed = tuple(([re.search('[^\n]*',currency)[0],re.search('[^\n]*',currency)[0]]) for currency in currency_list)

with open("bicicleteiros/static/lists/time_zone_list.txt", "r") as time_zone_list_file:
    time_zone_list = tuple(time_zone_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    time_zone_list_fixed = tuple(([re.search('[^\n]*',time_zone)[0],re.search('[^\n]*',time_zone)[0]]) for time_zone in time_zone_list)

# Create your models here.
day_type_choices = (
    ('resting','resting'),
    ('cycling', 'cycling')
)

night_type_choices = (
    ('outside', 'outside'),
    ('accommodation', 'accommodation')
)
#---------------------------
expense_type_choices = (
    ('supermarket_expense', 'supermarket_expense'),
    ('restaurant_expense', 'restaurant_expense'),
    ('accommodation_expense', 'accommodation_expense'),
    ('transport_expense', 'transport_expense'),
    ('bureaucracy_expense', 'bureaucracy_expense'),
    ('other_expense', 'other_expense')
)

#Modelo para os comentarios:
class chat_comments_model(models.Model):
    comentario = models.TextField(blank=False)
    #Teño que utilizar DateField e non podo utilizar o DateTimeField porque na base de datos de Postgress
    #de Railway non me acepta o datetime field.
    #date_added = models.DateField (default=datetime.now, blank=True, null=True)
    date_added = models.DateTimeField (default=timezone.now, blank=True)
    username_comment = models.CharField(max_length=33, blank=True, null=True)
    number_of_replies = models.IntegerField(blank=True, null=True)

    #Esto é para que me ordene os comentarios na páxina por data. Os comentarios máis recentes que se posicionen arriba
    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return (str(self.pk))
    
#Modelo no que se gardarán as replies dos comentarios
class chat_comments_replies_model(models.Model):
    pk_original_comment = models.ForeignKey(chat_comments_model, on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now, blank=True)
    username_reply = models.CharField(max_length=33, blank=True, null=True)


class country_information_model(models.Model):
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True, unique=True)
    country_number = models.IntegerField(blank=False, null=False)
    capital_town = models.CharField(max_length=33, blank=True, null=True)
    surface = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_density = models.IntegerField(blank=True, null=True)
    rent_per_capita = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=50, choices= currency_list_fixed, blank=True, null=True)
    currency_change_euro = models.DecimalField(max_digits=15, decimal_places=5, blank = True, null=True, unique=True)
    time_zone = models.CharField(max_length=33, choices= time_zone_list_fixed, blank=True, null=True)
    visa_requerided = models.CharField(max_length=33, choices= (('yes', 'yes'), ('no','no')), blank=True, null=True)
    visa_price = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    visa_bribe = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)

    def __str__(self):
        return (self.country)  

#Agora obteño a semana na que estou dependendo da data de inicio
#We get the day of the year
#IMPORTANTE!!!: Eiqui tes que cambiar a data e por a data na que comezas a viaxe.
starting_day_of_year = datetime(2023,10,1).timetuple().tm_yday
current_day_of_year = datetime.now().timetuple().tm_yday
#Sumamos 1 para que o primer día me conte como o day 1
day_in_the_journey = (current_day_of_year - starting_day_of_year)+1
#Suamos 1 para que a primeira semana conte como semana 1 e non como semana 0.
week_day = ((current_day_of_year - starting_day_of_year)/7)+1

class money_model(models.Model):
    journey_day = models.IntegerField(default=int(day_in_the_journey), null=True)
    week = models.IntegerField(default=int(week_day), null=True) 
    country = models.ForeignKey(country_information_model, on_delete=models.PROTECT)
    country_number = models.IntegerField(blank=True, null=True)
    #Teño que duplicar o country_name porque á hora de tratar os datos, o country como ten un Foreign key móstrame un número no eixe x do gráfico e eu quero que me mostre o
    # nome do daís. E para que me mostre o nome do país o campo ten que ser un "CharField" e non un Foreign Key.
    # De todos os xeitos o "country_name" calcúlase automáticamente xa que colle o mesmo valor que o country.
    country_name = models.CharField(max_length=33, blank=True, null=True)
    expense = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    expense_type = models.CharField(max_length=33, choices=expense_type_choices, blank=True, null=True)
    expense_euros = models.IntegerField(blank = True, null=True)

    #Convert the money into Euros base on the currency change of the "country_information_model".
    def save(self):
        self.expense_euros = sum([self.expense*self.country.currency_change_euro])
        self.country_name = str(self.country)
        self.country_number = str(self.country.country_number)
        return super().save()

    def __str__(self):
        return (str(self.journey_day) + ' days ' + self.expense_type + ' ' + self.country_name)
    
class km_altitude_model (models.Model):
    journey_day = models.IntegerField(default=int(day_in_the_journey), null=True)
    week = models.IntegerField(default=int(week_day), null=True)
    country = models.ForeignKey(country_information_model, on_delete=models.PROTECT)
    country_number = models.IntegerField(blank=True, null=True)
    #Teño que duplicar o country_name porque á hora de tratar os datos, o country como ten un Foreign key móstrame un número no eixe x do gráfico e eu quero que me mostre o
    # nome do daís. E para que me mostre o nome do país o campo ten que ser un "CharField" e non un Foreign Key.
    # De todos os xeitos o "country_name" calcúlase automáticamente xa que colle o mesmo valor que o country.
    country_name = models.CharField(max_length=33, blank=True, null=True) 
    km_day = models.IntegerField(blank = True, null=True)
    altitude_day = models.IntegerField(blank = True, null=True)
    day_type = models.CharField(max_length=33, choices=day_type_choices, blank=True, null=True)
    night_type = models.CharField(max_length=33, choices=night_type_choices, blank=True, null=True)

    #Convert the money into Euros based on the currency change of the "country_information_model".
    def save(self):
        self.country_name = str(self.country)
        self.country_number = str(self.country.country_number)
        return super().save()
    
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




