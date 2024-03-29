from django.contrib import admin

from bicicleteiros.models import currency, country_information_model, money_model, km_altitude_model, chat_comments_model, chat_comments_replies_model, videos_model, photos_model

# Register your models here.

admin.site.register(currency)
#admin.site.register(country_information_model)
@admin.register(country_information_model)
class CountryInformationAdmin(admin.ModelAdmin):
    list_display = ['country', 'country_number']
admin.site.register(money_model)
admin.site.register(km_altitude_model)
admin.site.register(chat_comments_model)
admin.site.register(chat_comments_replies_model)
admin.site.register(videos_model)
admin.site.register(photos_model)


