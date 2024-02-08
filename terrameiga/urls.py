"""terrameiga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from registration.views import sign_in_view, sign_up_view, email_instructions_view, log_out_view, personal_data_view, password_update_view, delete_account_view, password_reset_view, password_new_password_view, password_reset_sent_view, sign_up_email_validation_confirmation_view, email_visualization_sign_up_view, email_visualization_password_recovery_view
from bicicleteiros.views import country_data_view, country_data_no_registered_view, iz_blog_portada_view, let_the_cycling_beging_blog_view, the_journey_to_the_journey_blog_view, preparation_preparation_blog_view, project_presentation_view, photos_view, videos_view, estadistica_plotly_view, estadistica_plotly_view_full_report
from tools.views import max_speed_slope_tool_view
# Vamos a importar varias views que xa está preconfiguradas por Django para gestionar o reseteo do password para cando o usuario se esqueza.
from django.contrib.auth import views as auth_views
#Con esto fago que na url aparezca a url e o idioma. Por exemplo: terrameiga.bike/gl/
from django.conf.urls.i18n import i18n_patterns


urlpatterns =   i18n_patterns (
    path('admin/', admin.site.urls),
    #BICICLETEIROS_URLs
    path('', country_data_no_registered_view, name="home_page_no_registered"),
    path('bicicleteiros/', country_data_view, name="bicleteiros_home_page"),
    path('bicicleteiros_statistics/', estadistica_plotly_view, name="bicicleteiros_estadistica_plotly"),
    path('bicicleteiros_statistics_full_report/', estadistica_plotly_view_full_report, name="bicicleteiros_estadistica_plotly_full_report"),
    path('bicicleteiros_pictures/', photos_view, name="bicicleteiros_photos"),
    path('bicicleteiros_videos/', videos_view, name="bicicleteiros_videos"),
    #PROFILE ACCOUNT
    path('account/personal_data/', personal_data_view, name="personal_data"),
    path('account/password/', password_update_view, name="password"),
    path('account/delete_account/', delete_account_view, name="delete_account"),
    #REGISTRATION_URLs
    path('sign_in/', sign_in_view, name="sign_in"),
    path('sign_up/', sign_up_view, name="sign_up"),
    #Google sign_up
    path('accounts/', include('allauth.urls')),
    path('account_confirmation_email_sent/', email_instructions_view, name="account_confirmation_email_sent"),
    path('account_confirmation_email_done/', email_visualization_sign_up_view, name="email_visualization_url"),
    path('account_confirmation_email_done/<uidb64>/<token>/', sign_up_email_validation_confirmation_view, name="sign_up_email_validation_confirmation"),
    path('account_password_email/', email_visualization_password_recovery_view, name="email_visualization_password_recovery_view"),
    #Para máis info sobre estas vistas perconfiguradas para manejar o reseteo de contraseñas, visita a documentación oficial de django
    #https://docs.djangoproject.com/en/4.2/topics/auth/default/
    # ou este vídeo: https://www.youtube.com/watch?v=sFPcd6myZrY
    path('reset_password/', password_reset_view, name="reset_password"),
    path('reset_password_sent/', password_reset_sent_view,  name="password_reset_done"),
    path('password_recovery_update/<uidb64>/<token>/', password_new_password_view, name="password_recovery_update"),
    path('log_out/', log_out_view, name="log_out"),
    #AGRADECEMENTOS
    path('people/', TemplateView.as_view(template_name = "people.html"), name="people"),
    #BLOG
    path('iz_blog/', iz_blog_portada_view, name="iz_blog"),
    path('iz_blog/let_the_cycling_begin/', let_the_cycling_beging_blog_view, name="let_the_cycling_begin"),
    path('the_journey_to_the_journey/', the_journey_to_the_journey_blog_view, name="the_journey_to_the_journey"),
    path('preparation_preparation_preparation/', preparation_preparation_blog_view, name="preparation_preparation"),
    path('new_year_country_plans/', TemplateView.as_view(template_name = "blog/blog_new_year_january.html"), name="new_year_country_plans_january_2024"),

    #TOOLS 
    path('tools/', max_speed_slope_tool_view, name="tool_speed"),
    path('gears/', TemplateView.as_view(template_name = "gear_blog.html"), name="gears"),
    path('info/', TemplateView.as_view(template_name = "info.html"), name="info"),
    
    #PROJECT PRESENTATION
    path('project_presentation/', project_presentation_view, name="project_presentation"),

    path('account/order/', TemplateView.as_view(template_name = "profile_account/order.html"), name="order"),
    path('account/returns/', TemplateView.as_view(template_name = "profile_account/returns.html"), name="returns"),
    path('product_1/', TemplateView.as_view(template_name = "product_detail.html"), name = "product_1"),
    path('riders/', TemplateView.as_view(template_name = "templates/riders.html"), name="riders"),
    path('registration_orixinal/', TemplateView.as_view(template_name = "templates/registration_orixinal.html"), name = "registration_orixinal"),
    path('castellano/', TemplateView.as_view(template_name = "templates/home_page.html"), name="home_page"),
    path('route/', TemplateView.as_view(template_name = "templates/route.html"), name="route"),
)

if settings.DEBUG:
    urlpatterns = list(urlpatterns) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = list(urlpatterns) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


