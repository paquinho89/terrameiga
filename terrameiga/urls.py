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
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from registration.views import sign_in_view, sign_up_view, log_out_view, personal_data_view, password_update_view, delete_account_view, password_reset_view, password_new_password_view, sign_up_email_validation_confirmation_view, profile_account, index
from newsletter.views import newsletter_home_page_view
from bicicleteiros.views import country_data_view
# Vamos a importar varias views que xa está preconfiguradas por Django para gestionar o reseteo do password para cando o usuario se esqueza.
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', newsletter_home_page_view, name="home_page"),
    path('sign_up/', sign_up_view, name="sign_up"),
    path('account_confirmation_email_sent/', TemplateView.as_view(template_name = "account_confirm_email_sent.html"), name="account_confirmation_email_sent"),
    path('account_confirmation_email_done/<uidb64>/<token>/', sign_up_email_validation_confirmation_view, name="sign_up_email_validation_confirmation"),
    path('sign_in/', sign_in_view, name="sign_in"),
    path('log_out/', log_out_view, name="log_out"),    
    path('account/personal_data/', personal_data_view, name="personal_data"),
    path('account/password/', password_update_view, name="password"),
    path('account/delete_account/', delete_account_view, name="delete_account"),
    #USER RESET PASSWORD URLs
    path('reset_password/', password_reset_view, name="reset_password"),
    #Para máis info sobre estas vistas perconfiguradas para manejar o reseteo de contraseñas, visita a documentación oficial de django
    #https://docs.djangoproject.com/en/4.2/topics/auth/default/
    # ou este vídeo: https://www.youtube.com/watch?v=sFPcd6myZrY
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),  name="password_reset_done"),
    path('reset_password/<uidb64>/<token>/', password_new_password_view, name="password_reset_confirm"),

    #BICICLETEIROS_URLs
    path('bicicleteiros/', country_data_view, name="bicleteiros_home_page"),

    path('account/order/', TemplateView.as_view(template_name = "profile_account/order.html"), name="order"),
    path('account/returns/', TemplateView.as_view(template_name = "profile_account/returns.html"), name="returns"),

    path('product_1/', TemplateView.as_view(template_name = "product_detail.html"), name = "product_1"),

    # Esta tamén a vamos a poder a eliminar path('profile_account/', profile_account, name="profile_account"),

    path('riders/', TemplateView.as_view(template_name = "templates/riders.html"), name="riders"),
    path('registration_orixinal/', TemplateView.as_view(template_name = "templates/registration_orixinal.html"), name = "registration_orixinal"),
    path('info/', TemplateView.as_view(template_name = "templates/info.html")),

    path('castellano/', index, name="home_page_es"),
    
    path('route/', TemplateView.as_view(template_name = "templates/route.html"), name="route"),

    path('xornadas/', TemplateView.as_view(template_name = "templates/xornadas_culturais.html"), name="info"),
    path('eliminar/', TemplateView.as_view(template_name = "templates/eliminar.html"), name="eliminar"),

]

if settings.DEBUG:
    urlpatterns = list(urlpatterns) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = list(urlpatterns) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


