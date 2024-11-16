from django.shortcuts import render
from .models import country_information_model, money_model, km_altitude_model, chat_comments_model, chat_comments_replies_model, videos_model, photos_model
from registration.models import CustomUser
from datetime import datetime, date
from django.db.models import Sum, Count
from bicicleteiros.forms import chat_replies_form, language_home_page_no_registration_form
from django.shortcuts import render, redirect
#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages
import re
from django.conf import settings
#Paquete para traducir texto que se xenera nas view. Neste caso é o texto das alertas
from django.utils.translation import gettext_lazy as _
#Con esto obteño o language que está identificando a función de django.middleware.locale.LocaleMiddleware (é un paquete que está no settings)
from django.utils.translation import get_language
from django.utils.translation import activate

from plotly.offline import plot
import plotly.express as px
import plotly.graph_objects as go

#Form for the newsletter
from newsletter.forms import form_newsletter

# Create your views here.
def country_data_no_registered_view (request):
    all_entry_days= money_model.objects.all()
    #Collemos a última entrada do día para que así podas incuir máis entradas co mesmo día. Podes ter dúas entradas de datos con día 41 porque nun mesmo día podes estar en máis dun país.
    all_entry_days_last=all_entry_days.first()
    #Da última entrada collemos do día collemos o día da viaxe na que estamos
    current_journey_day = all_entry_days_last.journey_day
    #Da última entrada collemos a semana
    current_week = all_entry_days_last.week
    #Da última entrada collemos o país
    #Teño que facer que sexa unha string porque senon dame problemas á hora de traducir o nome do país
    current_country = str(all_entry_days_last.country)
    country_number_country = country_information_model.objects.get(country= current_country).country_number
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    flag_url = str("country_flags/" + str(current_country).lower() + "-flag.gif")
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']

    #Eiqui o que fago é coller o idioma da url que me ven a través do request.
    initial_language = request.LANGUAGE_CODE
    #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
    form_language = language_home_page_no_registration_form(initial={'language': initial_language})
    if request.method == "POST":
        form_language = language_home_page_no_registration_form(data = request.POST)
        if form_language.is_valid():
            #print(request.POST)
            selected_language = form_language.cleaned_data['language']
            #Activate the language which was selected on the dropdown
            activate(selected_language)
            #Nesta sección o que fago e cambiar o idioma na url
            current_language = get_language()
            current_url = request.build_absolute_uri()
            new_url = re.sub(r'/[a-z]{2}/', f'/{current_language}/', current_url)
            return redirect(new_url)
    
    #Formulario da newsletter:
    newsletter_email = form_newsletter(data=request.POST)
    #Con esto o que fago é que o newsletter form se execute solo cando se clicka no subscribe button do html. Se non se non hai click no botón esta parte da view non se executa.
    #O que fago e que cando se executa o "newsletter" o form do idioma nunca vai ser válido, porque é un formulario que ten outro tipo de tigger. E entón pois esto so se vai executar
    #cando o form_language non é valido e o form da newsletter si.
    #Por outra parte, se eu executo solo o form language, ao ser este válido, o newsletter form non se vai a executar dentro da view
    if request.method == 'POST' and not form_language.is_valid():
        #Con esto asegúrome que o formulario da newsletter é executado solo cando ben do botón da subscription, comprobando que o 'newsletter_submitted" está presente no diccionario que nos da o request.POST.
        if newsletter_email.is_valid() and 'newsletter_submitted' in request.POST:
            #print(request.POST)
            # Create Comment object and save it on the database
            newsletter_email.save(commit=True)
            #Esto é para que me mostre a mensaxe de que se gardou/enviou a solicitude de contratación
            messages.success(request, _("Thanks for subscribe and being part of the bike travelling community"))
            return redirect('home_page_no_registered')
        else:
            # Eiqui o que fago e que recorra os distintos fields do form ("neste caso solo un") e que lle 
            # asigne o formato de error (O borde en vermello)
            for field, errors in newsletter_email.errors.items():
                newsletter_email[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
            messages.error(request, _("Check the errors and try again!"))
            #Cando o formulario ten un erro temos que volver cargar o idioma que o pillamos da url, polo tanto esto ponme no formulario do idioma, o mesmo idioma que hai na url
            form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})
            return redirect ('home_page_no_registered')
    
    context = {
        'journey_day_html' : current_journey_day ,
        'current_week_html' : current_week,
        'country_number_html' : country_number_country,
        'total_km_html' : total_km,
        'total_expenses_html' :total_money,
        'current_country_html' : current_country,
        'flag_url_html' : flag_url,
        'form_language_html' : form_language,
        'newsletter_email_html' : newsletter_email,
    }
    return render (request, 'bicicleteiros_home_page_no_registration.html', context)

def country_data_view (request):
    #PAra os que fan sign up con Google, cando se carga esta vista, gardo nos Account_settings o idioma que está na url sempre e cando o campo de language non esté baleiro.
    #E que se non fago esto, o campo do language queda vacío se se fai o sing_up con Google.
    current_user = CustomUser.objects.get(id=request.user.id)
    user_language = CustomUser.objects.get(email = current_user).language
    if user_language==None:
        current_user.language = request.LANGUAGE_CODE
        current_user.save()
    #-----GOOGLE AUTH---------------
    #Neste caso, como o usuario xa fixo log_in, eu vou coller o idioma que está nos seus Account Settings para meterllo a url e que se mostre todo no idioma correspondente
    user_language_2 = CustomUser.objects.get(email = current_user).language
    activate(user_language_2)
    #----------End GOOGLE AUTH--------------

    #Co request.user fago que solo os usuarios que están rexistrados podan acceder a páxina de bicicleteiros (na que se mostra a miña posición)
    #No caso de que non estén rexistrados, mándoos a páxina de home_page_no_registered.
    #if request.user.is_authenticated:
    all_entry_days= money_model.objects.all()
    #Collemos a última entrada do día para que así podas incluir máis entradas co mesmo día. Podes ter dúas entradas de datos con día 41 porque nun mesmo día podes estar en máis dun país.
    all_entry_days_last=all_entry_days.first()
    #Da última entrada collemos do día collemos o día da viaxe na que estamos
    current_journey_day = all_entry_days_last.journey_day
    #Da última entrada collemos a semana
    current_week = all_entry_days_last.week
    #Da última entrada collemos o país
    #Teño que facer que sexa unha string porque senon dame problemas á hora de traducir o nome do país
    current_country = str(all_entry_days_last.country)
    country_number_country = country_information_model.objects.get(country= current_country).country_number
    visa_required = country_information_model.objects.get(country = current_country).visa_requerided
    visa_price = country_information_model.objects.get(country = current_country).visa_price
    capital_city = country_information_model.objects.get(country = current_country).capital_town
    population_country = country_information_model.objects.get(country = current_country).population
    population_dens = country_information_model.objects.get(country = current_country).population_density
    life_expectancy_country = country_information_model.objects.get(country = current_country).life_expectancy
    surface_country = country_information_model.objects.get(country = current_country).surface
    currency_country = country_information_model.objects.get(country = current_country).currency
    time_zone_value = country_information_model.objects.get(country = current_country).time_zone
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']
    flag_url = str("country_flags/" + str(current_country).lower() + "-flag.gif")
    if get_language() == "en":
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_en
    elif get_language() == "es":
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_es
    elif get_language() == "gl":
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_gl
    elif get_language() == "eu":
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_eu
    elif get_language() == "ca":
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_ca
    else:
        interesting_fact_country = country_information_model.objects.get(country = current_country).interesting_fact_es
        
    spotify_song_country = country_information_model.objects.get(country = current_country).song_spotify
    spotify_song_code_country = spotify_song_country.rsplit("/",1)[1]
    #Con esto obteño o language que está identificando a función de django.middleware.locale.LocaleMiddleware no browser. Básicamente o idioma do browser.
    current_language_browser = get_language()[:2]
    # REPLIES of the CHAT:
    form_chat_reply = chat_replies_form(data = request.POST)
    if request.method == 'POST':
        #Check whether it is valid:
        if form_chat_reply.is_valid():
            #Collemos o texto do reply
            reply_text_var = form_chat_reply.cleaned_data.get('reply_text')
            #Collemos o pk que está gardado no campo 'pk_original_comment' do formulario 'form_chat_reply', porque no html coa axuda de Javascript autocompletaros o 'pk_original_comment'
            # do formulario co pk do comentario orixinal. Esto é algo que se fai no html (bicicleteiros_home_page.html)
            pk_original_comment_var = form_chat_reply.cleaned_data.get('pk_original_comment')
            # ESto é para que se asigne o reply ao comentario raíz. Fago que o 'original_comment' do modelo 'chat_comments_replies_model' sexa igual que o "comentario" do 'chat_comments_model'
            #Gardo os datos no modelo "chat_comments_replies_model". Nota, para o original_comment que é o campo común entre os 2 modelos ('chat_comments_replies_model' & 'chat_comments_model')
            #teño que meter o post_comment que é unha variable que collo anteriormente que ten o texto do comentario raíz
            new_instance_reply = chat_comments_replies_model (reply_text= reply_text_var, username_reply = request.user.username, pk_original_comment = pk_original_comment_var)
            new_instance_reply.save()
            #Filtramos polo pk_original comment para contar cantas replies hay de cada comentario raíz
            number_replies_per_comment = chat_comments_replies_model.objects.filter(pk_original_comment=new_instance_reply.pk_original_comment).count()
            #E despois actualizamos o modelo chat_comments_model co número de replies que ten cada comentario
            pk_of_the_comment_to_update=str(new_instance_reply.pk_original_comment)
            comment_entry_to_update = chat_comments_model.objects.filter(pk=pk_of_the_comment_to_update).first()
            #Actualizamos o comentario
            comment_entry_to_update.number_of_replies = number_replies_per_comment
            comment_entry_to_update.save()
            #Esto é para que me mostre a mensaxe de que se engadiu o reply
            messages.success(request, _('Thanks for your participation. Your reply has been successfully included!'))
            #artigos_content e que para que me retorne a vista do blog
            return redirect('bicleteiros_home_page')
            
        else:
            # Eiqui o que fago e que recorra os distintos fields do form ("neste caso solo un") e que lle 
            # asigne o formato de error (O borde en vermello)
            for field, errors in form_chat_reply.errors.items():
                form_chat_reply[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
            messages.error(request, _('Please, include some text in your reply'))

        #Eiqui o que fago e coller todos os comentarios que hai para mostralos na páxina eordénoos pondo os primeiros os máis recientes e despois xa tiro cos máis antigos
        chat_comments_all = chat_comments_model.objects.all().order_by('-date_added')
        #Contamos o número total de comentarios para polo na páxina
        number_comments=chat_comments_model.objects.all().count()
        #Eiqui collo as replies dos cometarios
        replies_comments_all = chat_comments_replies_model.objects.all()

        context = {
            'journey_day_html' : current_journey_day ,
            'current_week_html' : current_week,
            'country_number_html' : country_number_country,
            'total_km_html' : total_km,
            'total_money_html' : total_money,
            'current_country_html' : current_country,
            'visa_required_html' : visa_required,
            'visa_price_html' : visa_price,
            'flag_url_html' : flag_url,
            'capital_city_html' : capital_city,
            'surface_html' : surface_country,
            'population_html' : population_country,
            'density_population_html' : population_dens,
            'life_expectancy_country_html' : life_expectancy_country,
            'currency_html' : currency_country,
            'time_zone_html' : time_zone_value,
            'interesting_fact_country_html' : interesting_fact_country,
            'spotify_song_code_html' : spotify_song_code_country,
    
            'chat_comments_all_html' : chat_comments_all,
            'chat_number_comments_html' : number_comments,
            'form_chat_reply_html' : form_chat_reply,
            'replies_comments_all_html' : replies_comments_all,
            'current_language_browser_html' : current_language_browser,
            
            'graph_money_type_html' :all_entry_days
        }
        return render (request, 'bicicleteiros_home_page.html', context)
        
    #else:
        # User is not authenticated, redirect to the sign_in page
        #messages.error(request, _('You must be registered to access to this content. Go to terrameiga.bike/sign_up/ and create an account.'))
        #return redirect('sign_in')  # Change 'login' to your actual login URL name

def photos_view (request):
    #Collemos todos os links das imaxes que temos
    all_photos = photos_model.objects.all()
    #Poño nunha lista todos os países onde subín fotos de ese país.
    country_dict = {}
    for country_file_name in all_photos:
        country = str(country_file_name).rsplit(" ",1)[0]
        last_characters_file_name= str(country_file_name).rsplit("/",1)[-1]
        # Check if the country is already in the dictionary. If it is not in the dict, it creates a list for the new country where all the file_names are going to be stored for that country.
        # {'Spain': [list], 'France': [list]}
        if country not in country_dict:
            country_dict[country] = []
        #Append the file name to the list of each specific country
        country_dict[country].append(last_characters_file_name)
    print(country_dict.items())

    context = {
        'country_dict_html' : country_dict
    }
    return render(request, 'bicicleteiros_fotos.html', context)

def videos_view (request):
    #Co values_list e o flat=True obteño solo os links de YouTube que é o que me interesa.
    all_links = videos_model.objects.values_list('youtube_link', flat=True)
    list_link_last_characters = []
    for str_link in all_links:
        #Collemos solo o final do link de YoutTube que é onde está o código que me interesa.
        #last_characters = str_link.rsplit('-',1)[1]
        #last_characters = str_link.rsplit(Convert.ToChar(61), 1)(1)
        list_link_last_characters.append(str_link)
        
    context={
        'all_links_last_characters_html' : list_link_last_characters
    }

    return render (request, 'bicicleteiros_videos.html', context)


def estadistica_plotly_view(request):
    #--------------Getting the global metrics ------------------------------------
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    total_climbing_dictionary = km_altitude_model.objects.aggregate(Sum('altitude_day'))
    total_climbing = total_climbing_dictionary['altitude_day__sum']
    all_entry_days_last= money_model.objects.all().first()
    current_country = str(all_entry_days_last.country)
    country_number_country = country_information_model.objects.get(country= current_country).country_number
    current_journey_day = all_entry_days_last.journey_day
    resting_days= km_altitude_model.objects.filter(day_type="resting").count()
    cycling_days= km_altitude_model.objects.filter(day_type="cycling").count()
    night_outside= km_altitude_model.objects.filter(night_type="outside").count()
    night_inside= km_altitude_model.objects.filter(night_type="accommodation").count()
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']

    #--------------END Getting the global metrics ------------------------------------
    continent_color_map = {
        'Asia': '#EF553B',   
        'Europe': '#636EFA', 
        'America': '#00CC96',
        'Africa': '#2CA02C', 
    }
    #-----------------GRAPH KIND OF EXPENSES - PIE CHART---------------------------------
    qs_expenses_type = money_model.objects.values('expense_type').annotate(Sum('expense_euros'))

    fig_expenses_type = px.pie(qs_expenses_type,
                values='expense_euros__sum',  
                names='expense_type',
                title=str(_("Where does the money go?")),
                hover_data=['expense_type']
                )
    
    fig_expenses_type.update_traces(
        textposition='inside', 
        textinfo='percent+label+value',
        texttemplate='%{label}<br>%{value:.0f} Euros<br>%{percent:.0%}',
        hovertemplate='%{label}: %{value:.0f} Euros',
        )

    # Change the title font size
    fig_expenses_type.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#808080"),
        showlegend=False,
        height=500  # Adjust the height as needed
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    pie_chart_expenses_type = plot(fig_expenses_type, output_type='div')
    #-----------------END GRAPH KIND OF EXPENSES - PIE CHART---------------------------------

    #-----------------GRAPGH EXPENSES PER WEEK---------------------------------
    qs_expenses_week = money_model.objects.values('week', 'continent').annotate(Sum('expense_euros')).order_by('week')
    #Collemos as últimas 17 entradas para mostrar no gráfico.PONO ACTIVO CANDO TEÑAS MOITOS VALORES
    #qs_expenses_week = qs_expenses_week[len(qs_expenses_week)-17:]

    fig_expenses_week = px.bar(qs_expenses_week, 
                 y='expense_euros__sum', 
                 x='week', 
                 color='continent',
                 #text_auto='.2s',#Esto é para que aparece o dato na barra
                 color_discrete_map=continent_color_map,
                 title=str(_("Expenses per Week"))
                )

    # Force x-axis to be categorical
    fig_expenses_week.update_xaxes(type='category', title_text=str(_('Week')))
    #Esto é para cambiar o nome do eixo y
    fig_expenses_week.update_yaxes(title_text='Euros', showgrid=False, zeroline=False)
    # Change the hover label
    fig_expenses_week.update_traces(hovertemplate=str(_('Week: %{x}<br>Expense: %{y:.} Euros')))
    # Change the title font size
    fig_expenses_week.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    bar_chart_expenses_week = plot(fig_expenses_week, output_type='div') # Use plotly.offline.plot with output_type='div' to get the HTML div
    #-----------------END GRAPGH EXPENSES PER WEEK---------------------------------

    #-----------------GRAPGH EXPENSES PER COUNTRY---------------------------------
    qs_expenses_country = money_model.objects.values('country_name', 'continent').annotate(Sum('expense_euros')).order_by('country_number') #Se che da algún problema o orden dos países é porque o country_number é unha string
    #Collemos as últimas 15 entradas para mostrar no gráfico. PONO ACTIVO CANDO TEÑAS MOITOS VALORES
    #qs_expenses_country = qs_expenses_country[len(qs_expenses_country)-15:]

    fig_expenses_country = px.bar(qs_expenses_country, 
                 y='expense_euros__sum', 
                 x='country_name', 
                 color='continent',
                 #Esto é para que aparece o dato na barra
                 #text_auto='.2s',
                 color_discrete_map=continent_color_map,
                 title=str(_("Expenses per Country")))

    #Esto é para cambiar o nome do eixo y
    fig_expenses_country.update_xaxes(title_text=str(_('Country')))
    #Esto é para cambiar o nome do eixo y
    fig_expenses_country.update_yaxes(title_text='Euros', showgrid=False, zeroline=False)
    # Change the hover label
    fig_expenses_country.update_traces(hovertemplate=str(_('Country: %{x}<br>Expense: %{y:.} Euros')))
    # Change the title font size
    fig_expenses_country.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_chart_expenses_country = plot(fig_expenses_country, output_type='div')
    #-----------------END GRAPGH EXPENSES PER COUNTRY---------------------------------

    #-----------------GRAPGH KM AND ALTITUDE PER WEEK---------------------------------
    qs_km_meters_week = km_altitude_model.objects.values('week', 'continent').annotate(Sum('km_day'),Sum('altitude_day')).order_by('week')
    #Collemos as últimas 17 entradas para mostrar no gráfico. PONO ACTIVO CANDO TEÑAS MOITOS VALORES
    #qs_km_meters_week = qs_km_meters_week[len(qs_km_meters_week)-17:]

    fig_km_meters_week = px.bar(qs_km_meters_week, 
                 y='km_day__sum', 
                 x='week', 
                 color='continent',
                 color_discrete_map=continent_color_map,
                 title=str(_("Distance and altitude per week")),
                 custom_data=['altitude_day__sum']
                 )
    
    #fig_km_meters_week.add_trace(
                #go.Scatter(
                    #x=[item['week'] for item in qs_km_meters_week], 
                    #y=[item['altitude_day__sum'] for item in qs_km_meters_week], 
                    #mode='lines', 
                    #name=str(_('Climb')),
                    #xaxis='x',  # Set the line chart to use the primary x-axis
                    #yaxis='y2',
                    #customdata=[[item['altitude_day__sum']] for item in qs_km_meters_week],
                    #line=dict(color='#56ff00')))

    # Update layout to show the secondary y-axis
    fig_km_meters_week.update_layout(
        yaxis2=dict(
        title=str(_('Climb (meters)')),
        overlaying='y',
        side='right'
        )
    )
    # Force x-axis to be categorical
    fig_km_meters_week.update_xaxes(type='category')
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_week.update_xaxes(title_text=str(_('Week')))
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_week.update_layout(
        yaxis=dict(title_text=str(_('Distance (Km)')), showgrid=False, zeroline=False),
        yaxis2=dict(title_text=str(_('Climb (meters)')), overlaying='y', side='right', showgrid=False, zeroline=False)
        )
    # Change the hover label
    fig_km_meters_week.update_traces(hovertemplate=str(_('Week: %{x}<br>Km: %{y:.} km<br>Climb: %{customdata[0]:.} meters')))
    # Change the title font size
    fig_km_meters_week.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_km_meters_week = plot(fig_km_meters_week, output_type='div')
    #-----------------END GRAPGH KM AND ALTITUDE PER WEEK---------------------------------

    #-----------------GRAPGH KM AND ALTITUDE PER COUNTRY---------------------------------
    qs_km_meters_country = km_altitude_model.objects.values('country_name', 'continent').annotate(Sum('km_day'),Sum('altitude_day')).order_by('country_number') #Se che da algún problema o orden dos países é porque o country_number é unha string
    #Collemos as últimas 15 entradas para mostrar no gráfico. PONO ACTIVO CANDO TEÑAS MOITOS VALORES
    #qs_km_meters_country = qs_km_meters_country[len(qs_km_meters_country)-15:]
    fig_km_meters_country = px.bar(qs_km_meters_country, 
                 y='km_day__sum', 
                 x='country_name', 
                 color='continent',
                 color_discrete_map=continent_color_map,
                 title=str(_("Distance and climb per country")),
                 custom_data=['altitude_day__sum']
                 )
    
    #fig_km_meters_country.add_trace(
                #go.Scatter(
                    #x=[item['country_name'] for item in qs_km_meters_country], 
                    #y=[item['altitude_day__sum'] for item in qs_km_meters_country], 
                    #mode='lines',
                    #name=str(_('Climb')),
                    #xaxis='x',  # Set the line chart to use the primary x-axis
                    #yaxis='y2',
                    #customdata=[[item['altitude_day__sum']] for item in qs_km_meters_country],
                    #line=dict(color='#56ff00')))

    # Update layout to show the secondary y-axis
    fig_km_meters_country.update_layout(
        yaxis2=dict(
        title=str(_('Climb (meters)')),
        overlaying='y',
        side='right'
        )
    )
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_country.update_xaxes(title_text=str(_('Country')))
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_country.update_layout(
        yaxis=dict(title_text=str(_('Distance (Km)')), showgrid=False, zeroline=False),
        yaxis2=dict(title_text=str(_('Climb (meters)')), overlaying='y', side='right', showgrid=False, zeroline=False)
        )
    # Change the hover label
    fig_km_meters_country.update_traces(hovertemplate=str(_('Country: %{x}<br>Km: %{y:.} km<br>Climb: %{customdata[0]:.} meters')))
    # Change the title font size
    fig_km_meters_country.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h', title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_km_meters_country = plot(fig_km_meters_country, output_type='div')
    #-----------------END GRAPGH KM AND ALTITUDE PER COUNTRY---------------------------------

    context = {
        'total_km_html' : total_km,
        'total_climbing_html' : total_climbing,
        'country_number_country_html' : country_number_country,
        'current_journey_day_html' : current_journey_day,
        'resting_days_html' : resting_days,
        'cycling_days_html' : cycling_days,
        'night_outside_html' : night_outside,
        'night_inside_html' : night_inside,
        'total_money_html' : total_money,

        #CHARTS
        'bar_chart__expenses_week_html': bar_chart_expenses_week,
        'bar_chart_expenses_country_html' : bar_chart_expenses_country,
        'pie_chart_expenses_type_html' : pie_chart_expenses_type,
        'bar_km_meters_week_html' : bar_km_meters_week,
        'bar_km_meters_country_html' : bar_km_meters_country
    }

    return render(request, 'bicicleteiros_statics_plotly.html', context)



def estadistica_plotly_view_full_report(request):
    #--------------Getting the global metrics ------------------------------------
    total_km_dictionary = km_altitude_model.objects.aggregate(Sum('km_day'))
    total_km = total_km_dictionary['km_day__sum']
    total_climbing_dictionary = km_altitude_model.objects.aggregate(Sum('altitude_day'))
    total_climbing = total_climbing_dictionary['altitude_day__sum']
    all_entry_days_last= money_model.objects.all().first()
    current_country = str(all_entry_days_last.country)
    country_number_country = country_information_model.objects.get(country= current_country).country_number
    current_journey_day = all_entry_days_last.journey_day
    resting_days= km_altitude_model.objects.filter(day_type="resting").count()
    cycling_days= km_altitude_model.objects.filter(day_type="cycling").count()
    night_outside= km_altitude_model.objects.filter(night_type="outside").count()
    night_inside= km_altitude_model.objects.filter(night_type="accommodation").count()
    total_money_dict = money_model.objects.aggregate(Sum('expense_euros'))
    total_money = total_money_dict['expense_euros__sum']

    #--------------END Getting the global metrics ------------------------------------
    continent_color_map = {
        'Asia': '#EF553B',   
        'Europe': '#636EFA', 
        'America': '#00CC96',
        'Africa': '#2CA02C', 
    }
    #-----------------GRAPH KIND OF EXPENSES - PIE CHART---------------------------------
    qs_expenses_type = money_model.objects.values('expense_type').annotate(Sum('expense_euros'))

    fig_expenses_type = px.pie(qs_expenses_type,
                values='expense_euros__sum',  
                names='expense_type',
                title=str(_("Where does the money go?")),
                hover_data=['expense_type']
                )
    
    fig_expenses_type.update_traces(
        textposition='inside', 
        textinfo='percent+label+value',
        texttemplate='%{label}<br>%{value:.0f} Euros<br>%{percent:.0%}',
        hovertemplate='%{label}: %{value:.0f} Euros',
        )

    # Change the title font size
    fig_expenses_type.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="#808080"),
        showlegend=False,
        height=500  # Adjust the height as needed
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    pie_chart_expenses_type = plot(fig_expenses_type, output_type='div')
    #-----------------END GRAPH KIND OF EXPENSES - PIE CHART---------------------------------

    #-----------------GRAPGH EXPENSES PER WEEK---------------------------------
    qs_expenses_week = money_model.objects.values('week', 'continent').annotate(Sum('expense_euros'))

    fig_expenses_week = px.bar(qs_expenses_week, 
                 y='expense_euros__sum', 
                 x='week', 
                 color='continent',
                 #text_auto='.2s',#Esto é para que aparece o dato na barra
                 color_discrete_map=continent_color_map,
                 title=str(_("Expenses per Week"))
                )

    # Force x-axis to be categorical
    fig_expenses_week.update_xaxes(type='category', title_text=str(_('Week')))
    #Esto é para cambiar o nome do eixo y
    fig_expenses_week.update_yaxes(title_text='Euros', showgrid=False, zeroline=False)
    # Change the hover label
    fig_expenses_week.update_traces(hovertemplate=str(_('Week: %{x}<br>Expense: %{y:.} Euros')))
    # Change the title font size
    fig_expenses_week.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    bar_chart_expenses_week = plot(fig_expenses_week, output_type='div') # Use plotly.offline.plot with output_type='div' to get the HTML div
    #-----------------END GRAPGH EXPENSES PER WEEK---------------------------------

    #-----------------GRAPGH EXPENSES PER COUNTRY---------------------------------
    qs_expenses_country = money_model.objects.values('country_name', 'continent').annotate(Sum('expense_euros'))

    fig_expenses_country = px.bar(qs_expenses_country, 
                 y='expense_euros__sum', 
                 x='country_name', 
                 color='continent',
                 #Esto é para que aparece o dato na barra
                 #text_auto='.2s',
                 color_discrete_map=continent_color_map,
                 title=str(_("Expenses per Country")))

    #Esto é para cambiar o nome do eixo y
    fig_expenses_country.update_xaxes(title_text=str(_('Country')))
    #Esto é para cambiar o nome do eixo y
    fig_expenses_country.update_yaxes(title_text='Euros', showgrid=False, zeroline=False)
    # Change the hover label
    fig_expenses_country.update_traces(hovertemplate=str(_('Country: %{x}<br>Expense: %{y:.} Euros')))
    # Change the title font size
    fig_expenses_country.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_chart_expenses_country = plot(fig_expenses_country, output_type='div')
    #-----------------END GRAPGH EXPENSES PER COUNTRY---------------------------------

    #-----------------GRAPGH KM AND ALTITUDE PER WEEK---------------------------------
    qs_km_meters_week = km_altitude_model.objects.values('week', 'continent').annotate(Sum('km_day'),Sum('altitude_day'))

    fig_km_meters_week = px.bar(qs_km_meters_week, 
                 y='km_day__sum', 
                 x='week', 
                 color='continent',
                 color_discrete_map=continent_color_map,
                 title=str(_("Distance and altitude per week")),
                 custom_data=['altitude_day__sum']
                 )
    
    fig_km_meters_week.add_trace(
                go.Scatter(
                    x=[item['week'] for item in qs_km_meters_week], 
                    y=[item['altitude_day__sum'] for item in qs_km_meters_week], 
                    mode='lines', 
                    name=str(_('Climb')),
                    xaxis='x',  # Set the line chart to use the primary x-axis
                    yaxis='y2',
                    customdata=[[item['altitude_day__sum']] for item in qs_km_meters_week],
                    line=dict(color='#56ff00')))

    # Update layout to show the secondary y-axis
    fig_km_meters_week.update_layout(
        yaxis2=dict(
        title=str(_('Climb (meters)')),
        overlaying='y',
        side='right'
        )
    )
    # Force x-axis to be categorical
    fig_km_meters_week.update_xaxes(type='category')
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_week.update_xaxes(title_text=str(_('Week')))
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_week.update_layout(
        yaxis=dict(title_text=str(_('Distance (Km)')), showgrid=False, zeroline=False),
        yaxis2=dict(title_text=str(_('Climb (meters)')), overlaying='y', side='right', showgrid=False, zeroline=False)
        )
    # Change the hover label
    fig_km_meters_week.update_traces(hovertemplate=str(_('Week: %{x}<br>Km: %{y:.} km<br>Climb: %{customdata[0]:.} meters')))
    # Change the title font size
    fig_km_meters_week.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h',title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_km_meters_week = plot(fig_km_meters_week, output_type='div')
    #-----------------END GRAPGH KM AND ALTITUDE PER WEEK---------------------------------

    #-----------------GRAPGH KM AND ALTITUDE PER COUNTRY---------------------------------
    qs_km_meters_country = km_altitude_model.objects.values('country_name', 'continent').annotate(Sum('km_day'),Sum('altitude_day'))
    fig_km_meters_country = px.bar(qs_km_meters_country, 
                 y='km_day__sum', 
                 x='country_name', 
                 color='continent',
                 color_discrete_map=continent_color_map,
                 title=str(_("Distance and climb per country")),
                 custom_data=['altitude_day__sum']
                 )
    
    fig_km_meters_country.add_trace(
                go.Scatter(
                    x=[item['country_name'] for item in qs_km_meters_country], 
                    y=[item['altitude_day__sum'] for item in qs_km_meters_country], 
                    mode='lines',
                    name=str(_('Climb')),
                    xaxis='x',  # Set the line chart to use the primary x-axis
                    yaxis='y2',
                    customdata=[[item['altitude_day__sum']] for item in qs_km_meters_country],
                    line=dict(color='#56ff00')))

    # Update layout to show the secondary y-axis
    fig_km_meters_country.update_layout(
        yaxis2=dict(
        title=str(_('Climb (meters)')),
        overlaying='y',
        side='right'
        )
    )
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_country.update_xaxes(title_text=str(_('Country')))
    #Esto é para cambiar o nome do eixo y
    fig_km_meters_country.update_layout(
        yaxis=dict(title_text=str(_('Distance (Km)')), showgrid=False, zeroline=False),
        yaxis2=dict(title_text=str(_('Climb (meters)')), overlaying='y', side='right', showgrid=False, zeroline=False)
        )
    # Change the hover label
    fig_km_meters_country.update_traces(hovertemplate=str(_('Country: %{x}<br>Km: %{y:.} km<br>Climb: %{customdata[0]:.} meters')))
    # Change the title font size
    fig_km_meters_country.update_layout(
        title=dict(font=dict(size=20, color="#808080")),
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(x=0, y=-0.3, orientation='h', title = ''), # Adjust the position of the legend and change the title
        bargap=0, #Engadir ou eliminar o espazo entre as barras.
        bargroupgap=0,
        font=dict(color="#808080")
        )
    # Use plotly.offline.plot with output_type='div' to get the HTML div
    bar_km_meters_country = plot(fig_km_meters_country, output_type='div')
    #-----------------END GRAPGH KM AND ALTITUDE PER COUNTRY---------------------------------

    context = {
        'total_km_html' : total_km,
        'total_climbing_html' : total_climbing,
        'country_number_country_html' : country_number_country,
        'current_journey_day_html' : current_journey_day,
        'resting_days_html' : resting_days,
        'cycling_days_html' : cycling_days,
        'night_outside_html' : night_outside,
        'night_inside_html' : night_inside,
        'total_money_html' : total_money,

        #CHARTS
        'bar_chart__expenses_week_html': bar_chart_expenses_week,
        'bar_chart_expenses_country_html' : bar_chart_expenses_country,
        'pie_chart_expenses_type_html' : pie_chart_expenses_type,
        'bar_km_meters_week_html' : bar_km_meters_week,
        'bar_km_meters_country_html' : bar_km_meters_country
    }

    return render(request, 'bicicleteiros_statics_plotly_full_report.html', context)


def iz_blog_portada_view (request):
    #Esto é para o pequeno formulario do idioma que hay no footer da home_page_no_registration.
    form_language = language_home_page_no_registration_form(data = request.POST)
    if request.method == "POST":
        if form_language.is_valid():
            selected_language = form_language.cleaned_data['language']
            #Activate the language which was selected on the dropdown
            activate(selected_language)
    context = {
        'form_language_html' : form_language,
    }
    return render (request, 'blog/blog_iz_zoe_portada.html', context)

def let_the_cycling_beging_blog_view (request):
    #Esto é para o pequeno formulario do idioma que hay no footer da home_page_no_registration.
    form_language = language_home_page_no_registration_form(data = request.POST)
    if request.method == "POST":
        if form_language.is_valid():
            selected_language = form_language.cleaned_data['language']
            #Activate the language which was selected on the dropdown
            activate(selected_language)
    context = {
        'form_language_html' : form_language,
    }
    return render (request, 'blog/blog_let_the_cycling_begin.html', context)

def the_journey_to_the_journey_blog_view (request):
    #Esto é para o pequeno formulario do idioma que hay no footer da home_page_no_registration.
    form_language = language_home_page_no_registration_form(data = request.POST)
    if request.method == "POST":
        if form_language.is_valid():
            selected_language = form_language.cleaned_data['language']
            #Activate the language which was selected on the dropdown
            activate(selected_language)
    context = {
        'form_language_html' : form_language,
    }
    return render (request, 'blog/blog_the_journey_to_the_journey.html', context)

def preparation_preparation_blog_view (request):
    #Esto é para o pequeno formulario do idioma que hay no footer da home_page_no_registration.
    form_language = language_home_page_no_registration_form(data = request.POST)
    if request.method == "POST":
        if form_language.is_valid():
            selected_language = form_language.cleaned_data['language']
            #Activate the language which was selected on the dropdown
            activate(selected_language)
    context = {
        'form_language_html' : form_language,
    }
    return render (request, 'blog/blog_preparation_preparation.html', context)


def project_presentation_view (request):
    #Formulario IDIOMA
    #Eiqui o que fago é coller o idioma da url que me ven a través do request.
    initial_language = request.LANGUAGE_CODE
    #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
    form_language = language_home_page_no_registration_form(initial={'language': initial_language})
    if request.method == 'POST':
        form_language = language_home_page_no_registration_form(data = request.POST)
        if form_language.is_valid():
            selected_language = form_language.cleaned_data['language']
            activate(selected_language)
            
    context = {
        'form_language_html' : form_language,
    }
    return render (request, 'project_presentation.html', context)





