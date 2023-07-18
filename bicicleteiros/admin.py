from django.contrib import admin

from bicicleteiros.models import  summary_day_model, country_information_model

# Register your models here.

admin.site.register(summary_day_model)
admin.site.register(country_information_model)