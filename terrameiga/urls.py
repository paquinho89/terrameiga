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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name = "templates/home_page_galego.html"), name="home_page_gl"),
    path('castellano/', TemplateView.as_view(template_name = "templates/home_page_castellano.html"), name="home_page_es"),
    path('english/', TemplateView.as_view(template_name = "templates/home_page_english.html"), name="home_page_en"),

    path('route_gl/', TemplateView.as_view(template_name = "templates/route_gl.html"), name="route_gl"),

    path('info_gl/', TemplateView.as_view(template_name = "templates/info_gl.html"), name="info_gl"),

    path('sign_in_gl/', TemplateView.as_view(template_name = "templates/sign_in_gl.html"), name="sign_in_gl"),

    path('registration_gl/', TemplateView.as_view(template_name = "templates/registration_1_gl.html"), name="registration_gl"),

    path('profile_account_gl/', TemplateView.as_view(template_name = "templates/profile_account_gl.html"), name="profile_account_gl"),

    path('riders_gl/', TemplateView.as_view(template_name = "templates/riders_gl.html"), name="riders_gl"),

]

if settings.DEBUG:
    urlpatterns = list(urlpatterns) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = list(urlpatterns) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


