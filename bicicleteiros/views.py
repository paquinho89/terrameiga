from django.shortcuts import render
from .models import country_information_model
from datetime import datetime, date

# Create your views here.

def country_data_view (request):
    #country = country_information_model.objects.get (country ="France" )
    today = datetime.now().date()
    #TES QUE POR EIQUI O DÍA QUE COMEZAS A TÚA VIAXE.
    starting_date = datetime(2023, 7, 2).date()
    day_in_journey = today - starting_date
    print(type(day_in_journey))
    day_in_journey_just_days = str(day_in_journey).split(",",1)[0]
    context = {
        #'country_html' : country,
        'journey_day_html' : day_in_journey_just_days
    }
    return render (request, 'bicicleteiros_home_page.html', context)

