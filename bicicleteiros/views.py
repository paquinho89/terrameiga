from django.shortcuts import render
from .models import country_information_model, money_model, km_altitude_model, starting_date
from datetime import datetime, date
from django.db.models import Sum, Count
from django.http import JsonResponse

# Create your views here.

def country_data_view (request):
    all_entry_days= money_model.objects.all()
    #Collemos a última entrada do día para que así podas incuir máis entradas co mesmo día. Podes ter dúas entradas de datos con día 41 porque nun mesmo día podes estar en máis dun país.
    all_entry_days_last=all_entry_days.last()
    #Da última entrada collemos do día collemos o día da viaxe na que estamos
    current_journey_day = all_entry_days_last.journey_day
    #Da última entrada collemos o país
    current_country = all_entry_days_last.country
    country_number_country = country_information_model.objects.get(country= current_country).country_number
    visa_required = country_information_model.objects.get(country = current_country).visa_requerided
    visa_price = country_information_model.objects.get(country = current_country).visa_price
    capital_city = country_information_model.objects.get(country = current_country).capital_town
    population_country = country_information_model.objects.get(country = current_country).population
    population_dens = country_information_model.objects.get(country = current_country).population_density
    rent_per_capita_country = country_information_model.objects.get(country = current_country).rent_per_capita
    surface_country = country_information_model.objects.get(country = current_country).surface
    currency_country = country_information_model.objects.get(country = current_country).currency
    currency_country = country_information_model.objects.get(country = current_country).currency
    time_zone_value = country_information_model.objects.get(country = current_country).time_zone
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    flag_url = str("/static/country_flags/" + str(current_country).lower() + "-flag.gif")
    #annotate is the same as doing a 'group_by'
    money_per_day = money_model.objects.values(str('journey_day')).annotate(Sum('expense_euros'))
    money_per_country = money_model.objects.values(str('country_name')).annotate(Sum('expense_euros')).order_by('country_number')
    money_type = money_model.objects.values(str('expense_type')).annotate(Sum('expense_euros'))
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']
    km_altitude_per_day = km_altitude_model.objects.values(str('journey_day')).annotate(Sum('km_day'),Sum('altitude_day'))
    km_altitude_per_country = km_altitude_model.objects.values(str('country_name')).annotate(Sum('km_day'),Sum('altitude_day')).order_by('country_number')
    print(km_altitude_per_country)
    


    graph_country_data = country_information_model.objects.all()
    #graph_day_data = summary_day_model.objects.all()
    
    context = {
        'journey_day_html' : current_journey_day ,
        'country_number_html' : country_number_country,
        'total_km_html' : total_km,
        'current_country_html' : current_country,
        'visa_required_html' : visa_required,
        'visa_price_html' : visa_price,
        'flag_url_html' : flag_url,
        'capital_city_html' : capital_city,
        'surface_html' : surface_country,
        'population_html' : population_country,
        'density_population_html' : population_dens,
        'rent_per_capita_html' : rent_per_capita_country,
        'currency_html' : currency_country,
        'time_zone_html' : time_zone_value,

        'graph_money_per_day_html' : money_per_day,
        'graph_money_per_country_html': money_per_country,
        'graph_money_per_type_html': money_type,
        'graph_total_money_html': total_money,
        'graph_km_altitud_per_day_html': km_altitude_per_day,
        'graph_km_altitud_per_country_html': km_altitude_per_country,
        
        
        'graph_money_type_html' :all_entry_days
    }
    return render (request, 'bicicleteiros_home_page.html', context)

# def money_per_km_graph_view (request):
#     m = country_information_model.objects.all()
#     print(m)
#     context = {
#         'data_info': m
#     }
#     return (request, 'bicicleteiros_home_page.html', context)
    # Returninn Json data as Json is the data is the javasrpit object notation which allow us use the data in javasrit so
    # in the html file as well.
    # This is a http response but in Json way.
    #return JsonResponse(data)

