from django.db import models
import re
from datetime import datetime


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


class country_information_model(models.Model):
    country = models.CharField(max_length=33, choices= country_list_fixed, blank=True, null=True)
    capital_town = models.CharField(max_length=33, blank=True, null=True)
    surface = models.IntegerField(blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    population_density = models.IntegerField(blank=True, null=True)
    rent_per_capita = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=50, choices= currency_list_fixed, blank=True, null=True)
    currency_change_euro = models.DecimalField(max_digits=15, decimal_places=5, blank = True, null=True)
    time_zone = models.CharField(max_length=33, choices= time_zone_list_fixed, blank=True, null=True)
    visa_requerided = models.CharField(max_length=33, choices= (('yes', 'yes'), ('no','no')), blank=True, null=True)
    visa_price = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    visa_bribe = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)

    def __str__(self):
        return (self.country)  

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
    money_supermarket = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_restaurant = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_accommodation = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_equipment = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_transport = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_burocracy = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    money_others = models.DecimalField(max_digits=15, decimal_places=2, blank = True, null=True)
    total_money = models.IntegerField(blank = True, null=True)
    #currency cambiado a Euros
    currency_change = models.ForeignKey(country_information_model, on_delete=models.CASCADE)
    
    km_day = models.IntegerField(blank = True, null=True)
    altitude_day = models.IntegerField(blank = True, null=True)

    #Sum all the money from the different sources to auto-populate the "total_money" column with the sum of all the money spent in that day.
    def save(self):
        self.total_money = sum([self.money_supermarket, self.money_restaurant, self.money_accommodation, self.money_equipment, self.money_transport, self.money_burocracy, self.money_others])
        return super().save()

    def __str__(self):
        return (str(self.journey_day_model) + ' days' )
    





