from django.shortcuts import render, redirect
import math 
from .forms import wattios_form, weight_form, groupset_brand_form, groupset_model_form, teeth_chainring_form, teeth_cassette_form

def max_speed_slope_tool_view (request):
    wattios_input = wattios_form(request.POST)
    weight_input = weight_form(request.POST)
    groupset_brand_input =  groupset_brand_form (request.POST)
    groupset_model_input = groupset_model_form (request.POST)
    teeth_chainring_input = teeth_chainring_form(request.POST)
    teeth_cassette_input = teeth_cassette_form(request.POST)
    # Provide default values to avoid the errors
    speed_km_h = 0
    force_back_wheel = 0
    force_slope = 0
    slope_percentage = 0
    pendiente_por_cada_cassette = 0
    if request.method == 'POST':
        if wattios_input.is_valid() and weight_input.is_valid() and groupset_brand_input.is_valid() and groupset_model_input.is_valid() and teeth_chainring_input.is_valid() and teeth_cassette_input.is_valid():
            groupset_brand_value = groupset_brand_input.cleaned_data.get('groupset_brand')
            groupset_model_value = groupset_model_input.cleaned_data.get('groupset_model')
            teeth_chainring_value = teeth_chainring_input.cleaned_data.get('teeth_chainring')
            # Con esto covirto a teeth_cassette_value que é unha string a unha tupla para poder acceder aos seus valores
            teeth_chainring_value_list = teeth_chainring_value.strip('()').split(',')
            #Convertimos os elementos da lista que son strings a floats.
            teeth_chainring_value_list_float = [float(x) for x in teeth_chainring_value_list]
            teeth_cassette_value = teeth_cassette_input.cleaned_data.get('teeth_cassette')
            # Con esto convirto a teeth_cassette_value que é unha string a unha tupla para poder acceder aos seus valores
            teeth_cassette_value_list = teeth_cassette_value.strip('()').split(',')
            #Eiqui tamén temos que convertir os elementos da lista que son strings a floats.
            teeth_cassette_value_list_float = [float(x) for x in teeth_cassette_value_list]
            # #-----------------------------Calculo da velocidade máxima a unhas determinadas revolcuiós por min------------------------------------
            diameter_wheel_mm = 700
            rpm_chainring = 130
            #Fórmula para calcular o radio cos dentes do plato. s(é a distancia de punta a punta de cada dente. Vamos a supor 12,75mm). radio=s/2sen(pi/número dentes)
            diameter_chainring_mm =  [(12.75/(2*math.sin(math.pi/x)))*2 for x in teeth_chainring_value_list_float]
            diameter_cassete_mm = [(12.75/(2*math.sin(math.pi/x)))*2 for x in teeth_cassette_value_list_float]
            #---------------------------------------------------Variables para calcular a máxima pendente que o cilcista pode subir---------------------------------------
            wattios_kg_value = float(wattios_input.cleaned_data.get('wattios'))
            weight_person_kg_value = float(weight_input.cleaned_data.get('weight'))
            speed_ms = 1
            crankarm_metros = 165*0.001
            radio_back_wheel_metros = 700*0.001/2
            gravity = 9.8
            peso_exerce_ciclista = (wattios_kg_value*weight_person_kg_value)/(speed_ms*gravity)
            weight_bike_kg = 13 #Peso que supomos da bicicleta
            weight_bike_person = weight_person_kg_value + weight_bike_kg
            rolling_coefficient = 0.0085 #Este coeficiente é sobre asfalto
            force_slope = int(round((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient,0))

            #Para monoplato
            if len(diameter_chainring_mm) == 1:
                #-------------------Revolucións do cassette ou da roda (é o mesmo)------------------------
                rpm_cassette_1 = [(diameter_chainring_mm[0] * rpm_chainring)/x for x in diameter_cassete_mm] 
                #---------------------------Calculo da velocidade-----------------------------------------------
                distance_metros = 2*math.pi*(diameter_wheel_mm/2)/1000 # Distancia que se recorre cando a roda da unha volta
                meters_min_1 = [distance_metros*x for x in rpm_cassette_1] # metros que se recorren en 1 minuto
                speed_km_h = [round((x*60)/1000, 1) for x in meters_min_1] # Velocidade en km/h
                #--------------------Cálculo da máxima pendente que o ciclista pode subir----------------------
                radio_chainring_metros = (diameter_chainring_mm[0]*0.001)/2
                radio_cassete_metros = [(x*0.001)/2 for x in diameter_cassete_mm]
                tension_chain = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_chainring_metros
                force_back_wheel = [int(round(((x)/(radio_back_wheel_metros))*tension_chain, 0)) for x in radio_cassete_metros] #Forza que se transmite ao chao pola roda traseira por un ciclista
                # Calculamos a máxima pendiente que pode subir por aproximación
                pendiente_por_cada_cassette = []
                slope_percentage = 0 #Sempre ten que ser cero para que comece a subir a pendiente de tal forma a buscar o valor de pendiente por aproximación
                for x_force_back_wheel in force_back_wheel:
                    while not math.isclose (force_slope, x_force_back_wheel):
                        #Newtons que fan falta para mover bicicleta+persoa por unha subida.
                        force_slope = int((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient)
                        slope_percentage= slope_percentage + 0.1
                    print(slope_percentage)
                    pendiente_por_cada_cassette.append(round(slope_percentage,1))
                print(pendiente_por_cada_cassette)
            
            #Con 2 platos
            elif len(diameter_chainring_mm) == 2:
                #-------------------Revolucións do cassette ou da roda (é o mesmo)------------------------
                #Dividimos o cassette en duas divisións, xa que hai dous platos
                marchas_cortas_cassette_mm = diameter_cassete_mm[:len(diameter_cassete_mm)//2]
                marchas_largas_cassette_mm = diameter_cassete_mm[len(diameter_cassete_mm)//2:]
                plato_pequeno_mm = diameter_chainring_mm[0]
                plato_grande_mm = diameter_chainring_mm[1]
                rpm_cassette_marchas_cortas = [(plato_pequeno_mm * rpm_chainring)/x for x in marchas_cortas_cassette_mm] # Revoluciós por minuto do ciclista
                rpm_cassette_marchas_largas = [(plato_grande_mm * rpm_chainring)/x for x in marchas_largas_cassette_mm]
                rpm_cassette_2 = rpm_cassette_marchas_cortas + rpm_cassette_marchas_largas
                #---------------------------Calculo da velocidade-----------------------------------------------
                distance_metros = 2*math.pi*(diameter_wheel_mm/2)/1000 # Distancia que se recorre cando a roda da unha volta
                meters_min_2 = [distance_metros*x for x in rpm_cassette_2] # metros que se recorren en 1 minuto
                speed_km_h = [round((x*60)/1000, 0) for x in meters_min_2] # Velocidade en km/h
                #----------------------------Cálculo da máxima pendiente que o ciclista pode subir-----------------------
                radio_plato_pequeno_metros = (plato_pequeno_mm*0.001)/2
                radio_plato_grande_metros = (plato_grande_mm*0.001)/2
                radio_cassette_metros_marchas_cortas = [(x*0.001)/2 for x in rpm_cassette_marchas_cortas]
                radio_cassette_metros_marchas_largas = [(x*0.001)/2 for x in rpm_cassette_marchas_largas]
                tension_chain_marchas_cortas = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_plato_pequeno_metros
                tension_chain_marchas_largas = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_plato_grande_metros
                force_back_wheel_marchas_cortas = [int(round(((x)/(radio_back_wheel_metros))*tension_chain_marchas_cortas, 0)) for x in radio_cassette_metros_marchas_cortas] #Forza que se transmite ao chao pola roda traseira por un ciclista
                force_back_wheel_marchas_largas = [int(round(((x)/(radio_back_wheel_metros))*tension_chain_marchas_largas, 0)) for x in radio_cassette_metros_marchas_largas]
                total_forces_back_wheel = sorted(force_back_wheel_marchas_cortas + force_back_wheel_marchas_largas)
                # Calculamos a máxima pendiente que pode subir por aproximación
                pendiente_por_cada_cassette = []
                slope_percentage = 0 #Sempre ten que ser cero para que comece a subir a pendiente de tal forma a buscar o valor de pendiente por aproximación
                for x_force_back_wheel in total_forces_back_wheel:
                    while not math.isclose (force_slope, x_force_back_wheel):
                        #Newtons que fan falta para mover bicicleta+persoa por unha subida.
                        force_slope = int((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient)
                        slope_percentage= slope_percentage + 0.1
                    print(slope_percentage)
                    pendiente_por_cada_cassette.append(round(slope_percentage,1))
                print(pendiente_por_cada_cassette)
            elif len(diameter_chainring_mm) == 3:
                #-------------------Revolucións do cassette ou da roda (é o mesmo)------------------------
                #Dividimos o cassette en 3 divisións, xa que hai 3 platos
                marchas_cortas_cassette_mm_3 = diameter_cassete_mm [:len(diameter_cassete_mm)//3]
                marchas_medias_cassette_mm_3 = diameter_cassete_mm [len(diameter_cassete_mm)//3:2*len(diameter_cassete_mm)//3]
                marchas_largas_cassette_mm_3 = diameter_cassete_mm [2*len(diameter_cassete_mm)//3:]
                plato_pequeno_mm_3 = diameter_chainring_mm [0]
                plato_mediano_mm_3 = diameter_chainring_mm [1]
                plato_grande_mm_3 = diameter_chainring_mm  [2]
                rpm_cassette_marchas_cortas_3 = [(plato_pequeno_mm_3*rpm_chainring)/x for x in marchas_cortas_cassette_mm_3]
                rpm_cassette_marchas_intermedias_3 = [(plato_mediano_mm_3*rpm_chainring)/x for x in marchas_medias_cassette_mm_3]
                rpm_cassette_marchas_largas_3 = [(plato_grande_mm_3*rpm_chainring)/x for x in marchas_largas_cassette_mm_3]
                rpm_cassette_3 = rpm_cassette_marchas_cortas_3 + rpm_cassette_marchas_intermedias_3 + rpm_cassette_marchas_largas_3
                #---------------------------Calculo da velocidade-----------------------------------------------
                distance_metros = 2*math.pi*(diameter_wheel_mm/2)/1000 # Distancia que se recorre cando a roda da unha volta
                meters_min_3 = [distance_metros*x for x in rpm_cassette_3] # metros que se recorren en 1 minuto
                speed_km_h = [round((x*60)/1000,0) for x in meters_min_3] # Velocidade en km/h
                print(speed_km_h)
                #----------------------------Cálculo da máxima pendiente que o ciclista pode subir-----------------------
                radio_plato_pequeno_metros_3 = (plato_pequeno_mm_3*0.001)/2
                radio_plato_mediano_metros_3 = (plato_mediano_mm_3*0.001)/2
                radio_plato_grande_metros_3 = (plato_grande_mm_3*0.001)/2
                radio_cassette_metros_marchas_cortas_3 = [(x*0.001)/2 for x in rpm_cassette_marchas_cortas_3]
                radio_cassette_metros_marchas_intermedias_3 = [(x*0.001)/2 for x in rpm_cassette_marchas_intermedias_3]
                radio_cassette_metros_marchas_largas_3 = [(x*0.001)/2 for x in rpm_cassette_marchas_largas_3]
                tension_chain_marchas_cortas_3 = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_plato_pequeno_metros_3
                tension_chain_marchas_intermedias_3 = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_plato_mediano_metros_3
                tension_chain_marchas_largas_3 = (crankarm_metros*peso_exerce_ciclista*gravity)/radio_plato_grande_metros_3
                force_back_wheel_marchas_cortas_3 = [int(round(((x)/(radio_back_wheel_metros))*tension_chain_marchas_cortas_3, 0)) for x in radio_cassette_metros_marchas_cortas_3] #Forza que se transmite ao chao pola roda traseira por un ciclista
                force_back_wheel_marchas_intermedias_3 = [int(round(((x)/(radio_back_wheel_metros))*tension_chain_marchas_intermedias_3, 0)) for x in radio_cassette_metros_marchas_intermedias_3]
                force_back_wheel_marchas_largas_3 = [int(round(((x)/(radio_back_wheel_metros))*tension_chain_marchas_largas_3, 0)) for x in radio_cassette_metros_marchas_largas_3]
                total_forces_back_wheel_3 = sorted(force_back_wheel_marchas_cortas_3 + force_back_wheel_marchas_intermedias_3 + force_back_wheel_marchas_largas_3)
                # Calculamos a máxima pendiente que pode subir por aproximación
                pendiente_por_cada_cassette = []
                slope_percentage = 0 #Sempre ten que ser cero para que comece a subir a pendiente de tal forma a buscar o valor de pendiente por aproximación
                for x_force_back_wheel in total_forces_back_wheel_3:
                    while not math.isclose (force_slope, x_force_back_wheel):
                        #Newtons que fan falta para mover bicicleta + persoa por unha subida.
                        force_slope = int((weight_bike_person*gravity*math.sin(math.atan(slope_percentage/100)))+(weight_bike_person*gravity*math.cos(math.atan(slope_percentage/100)))*rolling_coefficient)
                        slope_percentage= slope_percentage + 0.1
                    print(slope_percentage)
                    pendiente_por_cada_cassette.append(round(slope_percentage,1))
                print(pendiente_por_cada_cassette)
  
    context = {
      'wattios_input_html': wattios_input,
      'weight_input_html' : weight_input,
      'groupset_brand_input_html' : groupset_brand_input,
      'groupset_model_input_html' : groupset_model_input,
      'teeth_chainring_input_html' : teeth_chainring_input,
      'teeth_cassette_input_html' : teeth_cassette_input,

      'speed_km_h_html':speed_km_h,
      'force_back_wheel_html' : force_back_wheel,
      'force_slope_html': force_slope,
      'pendiente_por_cada_cassette_html': pendiente_por_cada_cassette
    }
    return render (request, 'tool_speed.html', context)
         



