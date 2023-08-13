from django.contrib import admin

from bicicleteiros.models import country_information_model, money_model, km_altitude_model

# Register your models here.

admin.site.register(country_information_model)
admin.site.register(money_model)
admin.site.register(km_altitude_model)
