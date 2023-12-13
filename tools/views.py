from django.shortcuts import render, redirect
import math 

def max_speed_view (request):
    diameter_wheel = 700
    rpm_plate = 100
    diameter_plate =  160.3
    diameter_cassete = 103.7
    rpm_cassete = (diameter_plate * rpm_plate)/diameter_cassete
    print(rpm_cassete)
    distance_metros = 2*math.pi*(diameter_wheel/2)/1000
    print(distance_metros)
    meters_1_min = distance_metros*rpm_cassete
    speed_km_h = (meters_1_min*60)/1000
    print(speed_km_h)

    context = {
      'speed_km_h_html':speed_km_h
    }
    return render (request, 'tool_speed.html', context)


def max_slope_view (request):
    wattios_kg = 
    weight = 
    speed_m_s =  
    radio_plate =
    radio_cassete =
    distance_pedal =
    radio_back_wheel =

    diameter_cassete = 103.7
    rpm_cassete = (diameter_plate * rpm_plate)/diameter_cassete
    print(rpm_cassete)
    distance_metros = 2*math.pi*(diameter_wheel/2)/1000
    print(distance_metros)
    meters_1_min = distance_metros*rpm_cassete
    speed_km_h = (meters_1_min*60)/1000
    print(speed_km_h)

    context = {
      'speed_km_h_html':speed_km_h
    }
    return render (request, 'tool_speed.html', context)


