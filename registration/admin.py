from django.contrib import admin

# Register your models here para que aparezcan na páxina do admin
from .models import CustomUser

admin.site.register(CustomUser)
#from .models import sign_in_model
#admin.site.register(sign_in_model)
