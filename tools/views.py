from django.shortcuts import render, redirect
import math 
from .forms import wattios_form, weight_form, teeth_plate_form, teeth_cassette_form

def max_speed_view (request):
    wattios_input = wattios_form(request.POST)
    weight_input = weight_form(request.POST)
    teeth_plate_input = teeth_plate_form(request.POST)
    teeth_cassette_input = teeth_cassette_form(request.POST)
    if request.method == 'POST':
        if wattios_input.is_valid() and weight_input.is_valid() and teeth_plate_input.is_valid() and teeth_cassette_input.is_valid():
            wattios_value = wattios_input.cleaned_data.get('wattios')
            print('proooobadno', wattios_value)
            weight_value = weight_input.cleaned_data.get('weight')
            print('fora_peso', weight_value)
            teeth_plate_value = teeth_plate_input.cleaned_data.get('teeth_plate')
            print('teeth_plate', teeth_plate_value)
            teeth_cassette_value = teeth_cassette_input.cleaned_data.get('teeth_cassette')
            print(tuple(teeth_cassette_value))

    
    
    
    diameter_wheel_mm = 700
    rpm_plate = 100
    diameter_plate_mm =  160.3
    diameter_cassete_mm = 103.7
    rpm_cassete = (diameter_plate_mm * rpm_plate)/diameter_cassete_mm # Revoluciós por minuto do ciclista
    distance_metros = 2*math.pi*(diameter_wheel_mm/2)/1000 # Distancia que se recorre cando a roda da unha volta
    meters_1_min = distance_metros*rpm_cassete # metros que se recorren en 1 minuto
    speed_km_h = (meters_1_min*60)/1000 # Velocidade en km/h
    #print(speed_km_h)

    wattios_kg = 5
    weight_person_kg = 80
    speed_ms = 1  
    radio_plate_m = 160.3*0.001/2
    radio_cassete_m = 103.7*0.001/2
    distance_pedal_m = 150*0.001
    radio_back_wheel_m = 700*0.001/2
    gravity = 9.8
    peso_exerce_ciclista = (wattios_kg*weight_person_kg)/(speed_ms*gravity)
    tension_chain = ((distance_pedal_m)*peso_exerce_ciclista*gravity)/(radio_plate_m)
    force_back_wheel = int(round(((radio_cassete_m)/(radio_back_wheel_m))*tension_chain, 0)) #Forza que se transmite ao chao pola roda traseira por un ciclista con 1.8W/kg
    print('forza_roda_traseira', force_back_wheel)
    
    slope_percentage = 0 #Sempre ten que ser cero
    weight_bike_kg = 12
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
      'teeth_plate_input_html' : teeth_plate_input,
      'teeth_cassette_input_html' : teeth_cassette_input,

      'speed_km_h_html':speed_km_h,
      'force_back_wheel_html' : force_back_wheel,
      'force_slope_html': force_slope,
      'slope_percentage_html': int(round(slope_percentage,0))
    }
    return render (request, 'tool_speed.html', context)
         


