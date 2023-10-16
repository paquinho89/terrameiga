from django.shortcuts import render
from .models import country_information_model, money_model, km_altitude_model, starting_date, chat_comments_model, CustomUser
from datetime import datetime, date
from django.db.models import Sum, Count
from django.http import JsonResponse
from bicicleteiros.forms import chat_form
from django.shortcuts import render, redirect
#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages


# Create your views here.
def country_data_no_registered_view (request):
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
    time_zone_value = country_information_model.objects.get(country = current_country).time_zone
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    flag_url = str("/static/country_flags/" + str(current_country).lower() + "-flag.gif")
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']
    
    context = {
        'journey_day_html' : current_journey_day ,
        'country_number_html' : country_number_country,
        'total_km_html' : total_km,
        'total_expenses_html' :total_money,
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
        'time_zone_html' : time_zone_value
    }
    return render (request, 'bicicleteiros_home_page_no_registration.html', context)

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
    time_zone_value = country_information_model.objects.get(country = current_country).time_zone
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    flag_url = str("/static/country_flags/" + str(current_country).lower() + "-flag.gif")
    # Form configuration for the COMMENTS of the CHAT:
    form_chat = chat_form(data=request.POST)
    # if this is a POST request we need to process the form data (Todos os comentarions que nos cheguen serán POST)
    if request.method == 'POST':
        #Check whether it is valid:
        if form_chat.is_valid():
            post_comment = form_chat.cleaned_data.get('comentario')
            #Gardo o comentario e o user que puxo o comentario no modelo de "chat_comments_model". Desta forma podo mostar o usuario que puxo o comentario.
            new_instance = chat_comments_model (comentario= post_comment, username_comment = request.user.username)
            new_instance.save()
            #Esto é para que me mostre a mensaxe de que se gardou/enviou a solicitude de contratación
            messages.success(request, 'Grazas por participar nesta aventura e engadir o teu comentario!')
            #artigos_content e que para que me retorne a vista do blog
            return redirect('bicleteiros_home_page')
        else:
            #Comentando a seguinte línea o formulario non se vacía despois do error. 
            #newsletter_email = form_newsletter()
            # Eiqui o que fago e que recorra os distintos fields do form ("neste caso solo un") e que lle 
            # asigne o formato de error (O borde en vermello)
            for field, errors in form_chat.errors.items():
                form_chat[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
            #Esto imprime o error xusto debaixo do cajetín para inserir o correo
            messages.error(request, form_chat.errors)
            #messages.error(request, "Insira un enderezo de correo electrónico válido!")

    #Eiqui o que fago e coller todos os comentarios que hai para mostralos na páxina eordénoos pondo os primeiros os máis recientes e despois xa tiro cos máis antigos
    chat_comments_all = chat_comments_model.objects.all().order_by('-date_added')
    #Contamos o número total de comentarios para polo na páxina
    number_comments=chat_comments_model.objects.all().count()
    
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

        'chat_form_html': form_chat,
        'chat_comments_all_html' : chat_comments_all,
        'chat_number_comments_html' : number_comments,
        
        'graph_money_type_html' :all_entry_days
    }
    return render (request, 'bicicleteiros_home_page.html', context)



def estadistica_data_view (request):
    all_entry_days= money_model.objects.all()
    #annotate is the same as doing a 'group_by'
    money_per_day = money_model.objects.values(str('journey_day')).annotate(Sum('expense_euros'))
    money_per_country = money_model.objects.values(str('country_name')).annotate(Sum('expense_euros')).order_by('country_number')
    money_type = money_model.objects.values(str('expense_type')).annotate(Sum('expense_euros'))
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']
    km_altitude_per_day = km_altitude_model.objects.values(str('journey_day')).annotate(Sum('km_day'),Sum('altitude_day'))
    km_altitude_per_country = km_altitude_model.objects.values(str('country_name')).annotate(Sum('km_day'),Sum('altitude_day')).order_by('country_number')
    
    context = {

        'graph_money_per_day_html' : money_per_day,
        'graph_money_per_country_html': money_per_country,
        'graph_money_per_type_html': money_type,
        'graph_total_money_html': total_money,
        'graph_km_altitud_per_day_html': km_altitude_per_day,
        'graph_km_altitud_per_country_html': km_altitude_per_country,
        
        'graph_money_type_html' :all_entry_days
    }
    return render (request, 'bicicleteiros_estadísticas.html', context)

