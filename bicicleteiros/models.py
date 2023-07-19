from django.db import models
import re
from datetime import datetime


with open("bicicleteiros/static/lists/country_list.txt", "r") as country_list_file:
    country_list = tuple(country_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    country_list_fixed = tuple(([re.search('[^\n]*',country)[0],re.search('[^\n]*',country)[0]]) for country in country_list)

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

#THIS IS TO POPULATE THE DAY OF THE JOURNEY
#IMPORTANTE!!!: Eiqui tes que cambiar a data e por a data na que comezas a viaxe.
starting_date = datetime(2023, 7, 1).date()

today_date = datetime.now().date()
day_in_the_journey = today_date - starting_date
day_in_the_journey_final = str(day_in_the_journey).split(" ",1)[0]

class summary_day_model(models.Model):
    journey_day_model = models.IntegerField(default=int(day_in_the_journey_final), null=True) 
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    day_type = models.CharField(max_length=33, choices=day_type_choices, blank=True, null=True)
    night_type = models.CharField(max_length=33, choices=night_type_choices, blank=True, null=True)
    money_supermarket = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_restaurant = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_accommodation = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_equipment = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_transport = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_burocracy = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    money_others = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    #currency cambiado a Euros
    km_first_stop = models.IntegerField(blank = True, null=True)
    km_second_stop = models.IntegerField(blank = True, null=True)
    km_third_stop = models.IntegerField(blank = True, null=True)
    km_fourth_stop = models.IntegerField(blank = True, null=True)
    altitude_first_stop = models.IntegerField(blank = True, null=True)
    altitude_second_stop = models.IntegerField(blank = True, null=True)
    altitude_third_stop = models.IntegerField(blank = True, null=True)
    altitude_fourth_stop = models.IntegerField(blank = True, null=True)

    def __str__(self):
        return (str(self.journey_day_model) + ' day' )


class country_information_model(models.Model):
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    capital_town = models.CharField(max_length=33, blank=True, null=True)
    surface = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_density = models.IntegerField(blank=True, null=True)
    rent_per_capita = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    time_zone = models.CharField(max_length=33, choices= time_zone_list_fixed, blank=True, null=True)
    visa_requerided = models.CharField(max_length=33, choices= (('yes', 'yes'), ('no','no')), blank=True, null=True)
    visa_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (self.country)  
    
    #Calculate the surface_comparison_field (The comparison is done with Spain):
    # @property
    # def surface_comparison (self):
    #     return 41



