from django.contrib import admin

# Register your models here para que aparezcan na páxina do admin
from registration.models import CustomUser

@admin.register(CustomUser)
class users_registered(admin.ModelAdmin):
    list_display = ['email', 'username', 'language']
    search_fields = ['username']
