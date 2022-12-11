from django.contrib import admin

# Register your models here para que aparezcan na páxina do admin
from .models import rider_model

admin.site.register(rider_model)
