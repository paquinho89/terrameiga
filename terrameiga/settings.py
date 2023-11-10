"""
Django settings for terrameiga project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print ("base dir path", BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q=m#etp8+mf8)iu!a7+xs!*0$pc5j@_c5ndt^u77$vwq8+jwvc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Variable para activar o framework das alerts de django

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'products',
    'bicicleteiros',

]
# This is to indicate to Django that the user model is now this custom model (CustomeUser) instead of the User model
#IMPORTANTE! No caso de que "python manage.py migrate" non che funcione, referencialo a app que sexa.
# Algo como "python manage.py migrate registration"
AUTH_USER_MODEL = 'registration.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Esto é para detectar o idioma do usuario e que a páxina se moster no idioma que ten configurado
    #Se o non tes o idioma do usuario mostraráse o inglés por defecto
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'terrameiga.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #Indicamos hai que ir a buscar os templates
        'DIRS': [BASE_DIR / 'terrameiga/static/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'terrameiga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://www.vitainbeta.org/how-to-install-homebrew-on-mac-linux-windows/
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# To make the site available in other languages you have to install the gettext package following the video you have recorded
# https://www.youtube.com/watch?v=eMI2mE8rG5w
# Then run "python manage.py makemessages -l es" to create the .po file fot (in this case) Spanish as you can see at the end of the command "es"
# Then go to .po file and translate the text
# Then run the following command "python manage.py compilemessages" and the .mo file will be created.
# Then, if you change the language code to a language that you have made the translation, all the web, as well as the alerts will be transalated to the language you chose
# However, MIDDLEWARE, there is 'django.middleware.locale.LocaleMiddleware', which detects the language of the browser and put the webiste in the same language
# as the browser.

LANGUAGE_CODE = 'en-us'
#ESto é para o tema de ter múltiples idiomas na páxina web.
LOCALE_PATHS = [
   os.path.join(BASE_DIR, 'locale')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

#IMPORTANTE: o STATICFILES_DIRS é para indicar onde metes os arquivos estáticos
STATICFILES_DIRS=[
   BASE_DIR / "terrameiga/static/"
]

print("ruta do static_dir" ,STATICFILES_DIRS)

#MEDIA FILES: Estes son arquivos que suben os usuarios da web
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print('MEDIA URLS')
print(MEDIA_ROOT)
print(MEDIA_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#SMTP Configuration para envío de emails
# https://www.youtube.com/watch?v=sFPcd6myZrY
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'paquinho89@gmail.com'
EMAIL_HOST_PASSWORD = 'lfalufgrrjwftmsp'





