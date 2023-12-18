from django.shortcuts import render, redirect
import math 
from .forms import wattios_form, weight_form, teeth_chainring_form, teeth_2chainring_form, teeth_cassette_form

def max_speed_slope_tool_view (request):
    wattios_input = wattios_form(request.POST)
    weight_input = weight_form(request.POST)
    teeth_chainring_input = teeth_chainring_form(request.POST)
    teeth_2chainring_input = teeth_2chainring_form(request.POST)
    teeth_cassette_input = teeth_cassette_form(request.POST)
    # Provide default values to avoid the errors
    speed_km_h = 0
    force_back_wheel = 0
    force_slope = 0
    slope_percentage = 0
    if request.method == 'POST':
        if wattios_input.is_valid() and weight_input.is_valid() and teeth_chainring_input.is_valid() and teeth_2chainring_input.is_valid() and teeth_cassette_input.is_valid():
            wattios_value = float(wattios_input.cleaned_data.get('wattios'))
            weight_value = float(weight_input.cleaned_data.get('weight'))
            teeth_chainring_value = float(teeth_chainring_input.cleaned_data.get('teeth_chainring'))
            teeth_2chainring_value = teeth_2chainring_input.cleaned_data.get('teeth_2chainring')
            teeth_2chainring_value_small_mm = float(teeth_2chainring_value.strip('()').split(',')[0])
            teeth_2chainring_value_big_mm = float(teeth_2chainring_value.strip('()').split(',')[1])
            teeth_cassette_value = teeth_cassette_input.cleaned_data.get('teeth_cassette')
            #Con esto covirto a teeth_cassette_value que é unha string a unha tupla para poder acceder aos seus valores
            teeth_cassette_value_small_mm = float(teeth_cassette_value.strip('()').split(',')[0])
            teeth_cassette_value_big_mm = float(teeth_cassette_value.strip('()').split(',')[1])
            #-------------Calculo da velocidade máxima a unhas determinadas revolcuiós por min------------------------------------
            diameter_wheel_mm = 700
            rpm_chainring = 130
            diameter_chainring_mm =  teeth_chainring_value
            diameter_cassete_small_mm = teeth_cassette_value_small_mm
            rpm_cassete = (diameter_chainring_mm * rpm_chainring)/diameter_cassete_small_mm # Revoluciós por minuto do ciclista
            distance_metros = 2*math.pi*(diameter_wheel_mm/2)/1000 # Distancia que se recorre cando a roda da unha volta
            meters_1_min = distance_metros*rpm_cassete # metros que se recorren en 1 minuto
            speed_km_h = (meters_1_min*60)/1000 # Velocidade en km/h
            #print(speed_km_h)
            #--------------------Calculo da pendiente máxima que o ciclista pode ascender---------------------------------------------
            wattios_kg = wattios_value
            weight_person_kg = weight_value
            speed_ms = 1  
            radio_chainring_m = teeth_chainring_value*0.001/2
            radio_cassete_m_big = teeth_cassette_value_big_mm*0.001/2
            crankarm_m = 165*0.001
            radio_back_wheel_m = 700*0.001/2
            gravity = 9.8
            peso_exerce_ciclista = (wattios_kg*weight_person_kg)/(speed_ms*gravity)
            tension_chain = ((crankarm_m)*peso_exerce_ciclista*gravity)/(radio_chainring_m)
            force_back_wheel = int(round(((radio_cassete_m_big)/(radio_back_wheel_m))*tension_chain, 0)) #Forza que se transmite ao chao pola roda traseira por un ciclista con 1.8W/kg
            print('forza_roda_traseira', force_back_wheel)
    
            slope_percentage = 0 #Sempre ten que ser cero
            weight_bike_kg = 13 #Supomos a bicicleta sen peso
            weight_bike_person = weight_person_kg + weight_bike_kg
            rolling_coefficient = 0.0085 #Este coeficiente é sobre asfalto
            force_slope = int(round((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient,0))
            #Calculamos a máxima pendiente que pode subir por aproximación
            while not math.isclose (force_slope, force_back_wheel):
                #Newtons que fan falta para mover bicicleta+persoa por unha subida.
                force_slope = int((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient)
                slope_percentage= slope_percentage + 0.1
                #print(slope_percentage)
  
    context = {
      'wattios_input_html': wattios_input,
      'weight_input_html' : weight_input,
      'teeth_chainring_input_html' : teeth_chainring_input,
      'teeth_2chainring_input_html' : teeth_2chainring_input,
      'teeth_cassette_input_html' : teeth_cassette_input,

      'speed_km_h_html':speed_km_h,
      'force_back_wheel_html' : force_back_wheel,
      'force_slope_html': force_slope,
      'slope_percentage_html': int(round(slope_percentage,0))
    }
    return render (request, 'tool_speed.html', context)
         



