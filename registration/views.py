from django.shortcuts import render
from django.views.generic import View
from .forms import registration_form

# Create your views here.
def registration_view(request):
    registration_form_view = registration_form (data=request.POST)
    