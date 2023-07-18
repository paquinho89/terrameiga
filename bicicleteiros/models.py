from django.db import models
import re
from datetime import datetime


with open("bicicleteiros/static/lists/country_list.txt", "r") as country_list_file:
    country_list = tuple(country_list_file)
    #A regular expresion é para eliminar o salto de línea que contén toda a lista e que me funcione despois no formulario. Co [0] estou collendo o primer resultado da función re.search
    country_list_fixed = tuple(([re.search('[^\n]*',country)[0],re.search('[^\n]*',country)[0]]) for country in country_list)

# Create your models here.
day_type_choices = (
    ('resting','resting'),
    ('cycling', 'cycling')
)

night_type_choices = (
    ('outside', 'outside'),
    ('accommodation', 'accommodation')
)

#This is to prepopulate the day of the journey
today_date = datetime.now().date()
#IMPORTANTE: Eiqui tes que cambiar a data e por a data na que comezas a viaxe.
starting_date = datetime(2023, 7, 1).date()
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
    km_first_stop = models.IntegerField(blank = True, null=True)
    km_second_stop = models.IntegerField(blank = True, null=True)
    km_third_stop = models.IntegerField(blank = True, null=True)
    km_fourth_stop = models.IntegerField(blank = True, null=True)
    altitude_first_stop = models.IntegerField(blank = True, null=True)
    altitude_second_stop = models.IntegerField(blank = True, null=True)
    altitude_third_stop = models.IntegerField(blank = True, null=True)
    altitude_fourth_stop = models.IntegerField(blank = True, null=True)

    # @property
    # def journey_day (self):
    #     today = datetime.now().date()
    #     day_in_journey = today - self.starting_date
    #     day_in_journey_just_days = str(day_in_journey).split(",",1)[0]
    #     return day_in_journey_just_days


class country_information_model(models.Model):
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    rent_per_capita = models.IntegerField(blank=True, null=True)
    surface = models.IntegerField(blank=True, null=True)
    #surface_comparison with Spain
    regime = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    currency = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    #currency cambiado a Euros
    local_time = models.TimeField(blank = True, null = True)

    def __str__(self):
        return (self.country)  
    
    #Calculate the surface_comparison_field (The comparison is done with Spain):
    @property
    def surface_comparison (self):
        return 41



