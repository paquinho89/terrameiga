from django.shortcuts import render, redirect
from registration.forms import registration_form_1, registration_form_2, registration_form_3

# Create your views here.
def registration_view_1(request):
  # create a form instance and populate it with data from the request:
  registration_form_variable = registration_form_1(data=request.POST)
 
  context = {
        'form_1':registration_form_variable
  }
  return render (request, 'registration_1_gl.html', context)


def registration_view_2(request):
  # create a form instance and populate it with data from the request:
  registration_form_variable = registration_form_2(data=request.POST)
 
  context = {
        'form_2':registration_form_variable
  }
  return render (request, 'registration_2_gl.html', context)

def registration_view_3(request):
    # create a form instance and populate it with data from the request:
    registration_form_variable = registration_form_3(data=request.POST)

    context = {
        'form_3':registration_form_variable
    }
    return render (request, 'registration_3_gl.html', context)
    