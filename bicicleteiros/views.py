from django.shortcuts import render
from .models import country_information_model, summary_day_model, starting_date
from datetime import datetime, date
#Packages to create the local clock
# from tkinter  import *
# from tkinter.ttk import *
# from time import strftime

# root = Tk()
# root.title ("clock")

# label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
# label.pack(anchor='center')

# def local_clock ():
#     string = strftime('%H:%M:%S')
#     label.config(text=string)
#     label.after(1000, local_clock)

# label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
# label.pack(anchor='center')

# local_clock()
# mainloop()

# Create your views here.

def country_data_view (request):
    today = datetime.now().date()
    day_in_journey = today - starting_date
    day_in_journey_just_days = str(day_in_journey).split(",",1)[0]
    current_country = summary_day_model.objects.get(journey_day_model = day_in_journey_just_days.split(" ",1)[0] ).country
    capital_city = country_information_model.objects.get(country = current_country).capital_town
    population_country = country_information_model.objects.get(country = current_country).population
    population_dens = country_information_model.objects.get(country = current_country).population_density
    rent_per_capita_country = country_information_model.objects.get(country = current_country).rent_per_capita
    surface_country = country_information_model.objects.get(country = current_country).surface
    currency_country = country_information_model.objects.get(country = current_country).currency
    currency_country = country_information_model.objects.get(country = current_country).currency
    time_zone_value = country_information_model.objects.get(country = current_country).time_zone
    print(time_zone_value)
    
    context = {
        'journey_day_html' : day_in_journey_just_days,
        'current_country_html' : current_country,
        'capital_city_html' : capital_city,
        'surface_html' : surface_country,
        'population_html' : population_country,
        'density_population_html' : population_dens,
        'rent_per_capita_html' : rent_per_capita_country,
        'currency_html' : currency_country,
        'time_zone_html' : time_zone_value
    }
    return render (request, 'bicicleteiros_home_page.html', context)

