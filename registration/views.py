from django.shortcuts import render, redirect
from registration.forms import sign_in_form_1, sign_up_form_2, personal_data_form, password_update_form, delete_account_form, password_reset_form, password_new_form
#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages
#Esto carga un formulario que xa está preconfigurado para a autentificación do usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from bicicleteiros.forms import language_home_page_no_registration_form
#Esto é para que cargue un paquete que autentifique (para ver se o usuario está xa rexistrado na nosa base de datos), para que logee o usuario por nós e para lle faga log out
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .models import CustomUser
import re
from django.conf import settings
#This is to generate a random token which will be used in the url which will be sent to the email user to reset the password
import uuid
#Importamos un paquete para codificar o user_id (o pk) que vai na url que se lle envía ao usuario ao correo para resetear o contrasinal. O force bytes tamén e para codificar o pk
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .helpers import send_reset_password_mail, send_confirm_email
#Paquete para traducir texto que se xenera nas view. Neste caso é o texto das alertas
from django.utils.translation import gettext as _
#Con esto obteño o language que está identificando a función de django.middleware.locale.LocaleMiddleware (é un paquete que está no settings)
from django.utils.translation import get_language

from django.utils.translation import activate
from django.contrib.sites.shortcuts import get_current_site
from allauth.socialaccount.templatetags.socialaccount import provider_login_url
from django.db.models import Q



def sign_up_view(request):
  #-----GOOGLE AUTH---------------
  #Eiqui o que fago é coller o idioma da url que me ven a través do request.
  initial_language = request.LANGUAGE_CODE
  # Override the LOGIN_REDIRECT_URL. IMPORTANTE!! Esto faise para cando se faga o login con google (GoogleAUTH), se redireccione a páxina de bicicleteiros co correspondente idioma na url.
  settings.LOGIN_REDIRECT_URL = f"/{initial_language}/bicicleteiros/"
  #----------End GOOGLE AUTH-----------------
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST) 
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)
      #Nesta sección o que fago e cambiar o idioma na url
      current_language = get_language()
      current_url = request.build_absolute_uri()
      new_url = re.sub(r'/[a-z]{2}/', f'/{current_language}/', current_url)
      return redirect(new_url)
    
  # create a form instance and populate it with data from the request:
  sign_up_form_variable = sign_up_form_2(data=request.POST)
  if request.method == 'POST' and not form_language.is_valid():
    if sign_up_form_variable.is_valid():
      user_name = sign_up_form_variable.cleaned_data.get('username')
      #Con esto obtemos o email introducido no formulario, pero é o do tipo string e non me vale para obter o pk. É convertimolo a minúscula para que non de problemas.
      email_form_str = sign_up_form_variable.cleaned_data.get('email').lower()
      password_form = sign_up_form_variable.cleaned_data.get('password1')
      #Verficamos que o nome de usuario sexa único porque se quero que a xente tamén se logee con él, teño que facer que sexa único, igual que o email, que tamén é único
      all_user_names_list = CustomUser.objects.values_list('username', flat=True)
      if user_name in list(all_user_names_list):
        sign_up_form_variable['username'].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
        messages.add_message(request, messages.ERROR, _("Please, try again with a different username"))
      else:
        user = CustomUser.objects.create_user(user_name, email_form_str, password_form, language = str(get_language().rsplit("-")[0])) #Eiqui metémoslle o language que está habilitado no browser.
        #Con esto fago o usuario como non activo ata que confirme a súa conta de correo. Cando confime a conta o usario pasará a un estado de Activo.
        user.is_active = False
        user.save()
        #Con esto obtemos o email introducido no formulario pero este é do tipo "registration.models.CustomUser" que me vale para obter o pk do email
        email_form =  CustomUser.objects.filter(email=email_form_str).first()
        #This is to generate a random token to include in the link which will be sent to the customer and he/she will be able to reset the password.
        token = str(uuid.uuid4())
        #Con esto codificamos o user_id (pk) correspondente ao email incluido no formulario
        uidb64=urlsafe_base64_encode(force_bytes(email_form.pk))
        language = get_language()
        send_confirm_email (request, email_form, user_name, uidb64, token, language)
        #Esto é para que me mostre a mensaxe de que se fixo log-in correctamente
        messages.add_message(request, messages.SUCCESS, _("Please, go to your email and verify your account. Thanks for your support, ") + user_name)
        return redirect('account_confirmation_email_sent')
    else:
      # Eiqui o que fago e que recorra os distintos fields do form e que lle 
      # asigne o formato de error (O borde en vermello)
       for field, error in sign_up_form_variable.errors.items():
        sign_up_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
        #Solo me interesa o error, e eiqui é o que estou collerndo, a frase dos errores
        messages.add_message(request, messages.ERROR, _("Check the below errors and try again!"))
        #Cando o formulario ten un erro temos que volver cargar o idioma que o pillamos da url, polo tanto esto ponme no formulario do idioma, o mesmo idioma que hai na url
        form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})
    
       
  context = {
        'form_language_html': form_language,
        'sign_up_form':sign_up_form_variable
  }
  return render (request, '2_sign_up.html', context)

def email_visualization_sign_up_view (request):
  #Collemos os valores que veñen a través da url
  current_site = get_current_site(request)
  email_user = request.GET.get('email', None)
  nome = request.GET.get('username', None)
  uidb64_user = request.GET.get('uidb64_url', None)
  token_user =  request.GET.get('token_url', None)
  language_user = request.GET.get('language_url', None)

  sign_up_confirmation_link = f'http://{current_site}/{language_user}/account_confirmation_email_done/{uidb64_user}/{token_user}/'

  context = {
    'email_username_html': email_user,
    'username_html': nome,
    'sign_up_confirmation_link_html': sign_up_confirmation_link
  }
  return render(request, 'email_body_confirmation.html', context)

def email_instructions_view (request):
  #Eiqui o que fago é coller o idioma da url que me ven a través do request.
  initial_language = request.LANGUAGE_CODE
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST)
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)
    
  context = {
      'form_language_html' : form_language,
  }
  return render (request, 'account_confirm_email_sent.html', context)

def sign_up_email_validation_confirmation_view (request, uidb64, token):
  uid = force_str(urlsafe_base64_decode(uidb64))
  user = CustomUser.objects.get(pk=uid)
  #Cargamos a páxina no idioma que se gardou nas preferencias de usuario no momento que se fixo o sign_up. Recorda co email o único que fai é por en activo o usuario.
  user_language = CustomUser.objects.get(email = user).language
  activate(user_language)
  #Unha vez que clicka no link para verificar a súa conta, nos activamos o seu email.
  user.is_active = True
  #Ca conta do GoogleAuth tuven que por 2 backeds no settings file, con esto indico cal é o backend que
  #ten que utilizar cando se garden/cambien os atributos do personal data
  user.backend = 'django.contrib.auth.backends.ModelBackend'
  user.save()
  #NOTA interesante. Se queres coller algún atributo do usuario bastaría con escribir "user.password" ou "user.name"....
  #Con esta función fago log-in sen necesidade de introducir a contraseña. Ten en conta que eu nesta función non teño contraseña porque Django encríptaa e
  # non hai forma de desencriptala
  login(request, user)
  messages.add_message(request, messages.SUCCESS, _("Your account was succesfully created. Thanks for being part of this adventure!"))
  return redirect('bicleteiros_home_page')

def log_out_view (request):
   logout(request)
   messages.add_message(request, messages.SUCCESS, _("You have been logged out!"))
   return redirect('home_page_no_registered')

# Create your views here.
def sign_in_view(request):
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})
  if request.method == 'POST':
    #Esto é para o pequeno formulario do idioma que hay no footer da home_page_no_registration.
    form_language = language_home_page_no_registration_form(data = request.POST) 
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)
      #Nesta sección o que fago e cambiar o idioma na url
      current_language = get_language()
      current_url = request.build_absolute_uri()
      new_url = re.sub(r'/[a-z]{2}/', f'/{current_language}/', current_url)
      return redirect(new_url)
    
  sign_in_form_variable = sign_in_form_1(data=request.POST)
  #Con esto o que fago é que o sign_in_form se execute solo cando se clicka no sign_in_button do html. Se non se non hai click no botón esta parte da view non se executa.
  #O que fago e que cando se executa o "Sign In" o form do idioma nunca vai ser válido, porque é un formulario que ten outro tipo de tigger. E entón pois esto so se vai executar
  #cando o form_language non é valido e o sign si.
  #Por outra parte, se eu executo solo o form language, ao ser este válido, o sign-in form non se vai a executar dentro da view
  if request.method == 'POST' and not form_language.is_valid():
    sign_in_form_variable = sign_in_form_1(data=request.POST)
    if sign_in_form_variable.is_valid():
      #Non entendo mui ben porque para coller o email teño que collelo do username no form, pero ten que ser así para que funcione.
      email_or_username_form = sign_in_form_variable.cleaned_data.get('username')
      password_form = sign_in_form_variable.cleaned_data.get('password')
      #Para a xente que se logea co email
      if "@" in str(email_or_username_form):
        #Cando se faga o sign_in, vou buscar o idioma que ten o usuario configurado no seus datos (CustomUser model) e vouno activar.
        #Non quero que me cambie o idioma ao do browser, quero que me pille o que ten gardado no seu perfil
        user_language = CustomUser.objects.get(email = email_or_username_form).language
        activate(user_language)
        #Authenticate user returns the email of the user
        user_auth = authenticate(request, email=email_or_username_form, password=password_form)
        if user_auth is not None:
          login(request, user_auth)
          messages.success(request, _("Welcome! Now it's time to enjoy all the content from the journey."))
          return redirect('bicleteiros_home_page')
      #Para a xente que se logea co nome de usuario, collemos o seu nome de usario introducido e con eso sacamos o email para logearse.
      else:
        # Collemos o email na base de datos a través do username pero con un case insensitive.
        username_form = CustomUser.objects.filter(username__iexact=email_or_username_form).first()
        user_language = CustomUser.objects.get(email = username_form).language
        activate(user_language)
        #Authenticate user returns the email of the user
        user_auth = authenticate(request, email=username_form, password=password_form)
        if user_auth is not None:
          login(request, user_auth)
          messages.success(request, _("Welcome! Now it's time to enjoy all the content from the journey."))
          return redirect('bicleteiros_home_page')
    else:
      #Comento esto porque para o formulario que hai de AuthenticationForm preconfigurado por Django esto non me funciona.
      #for field, error in sign_in_form_variable.errors.items():
        # Eiqui o que fago e que recorra os distintos fields do form e que lle asigne o formato de error (O borde en vermello)
        #sign_in_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
        # Solo me interesa o error, e eiqui é o que estou collerndo, a frase dos errores
        #messages.add_message(request, messages.ERROR, error)
      messages.add_message(request, messages.ERROR, _("The email or the password are not correct. Try again, recover password or create a new TerraMeiga account"))
      #Cando o formulario ten un erro temos que volver cargar o idioma que o pillamos da url, polo tanto esto ponme no formulario do idioma, o mesmo idioma que hai na url
      form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})
      
  context = {
        "form_language_html" : form_language,
        "sign_in_form": sign_in_form_variable
  }
  return render (request, '1_sign_in.html', context)

from bicicleteiros.static.lists.country_list import country_list_values

def password_reset_view(request):
  #Formulario IDIOMA
  #Eiqui o que fago é coller o idioma da url que me ven a través do request.
  initial_language = request.LANGUAGE_CODE
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST)
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)
      #Nesta sección o que fago e cambiar o idioma na url
      current_language = get_language()
      current_url = request.build_absolute_uri()
      new_url = re.sub(r'/[a-z]{2}/', f'/{current_language}/', current_url)
      return redirect(new_url)
  
  password_recovery_form_variable = password_reset_form (data=request.POST)
  if request.method == "POST" and not form_language.is_valid():
    password_recovery_form_variable = password_reset_form (data=request.POST)
    if password_recovery_form_variable.is_valid():
      #Con esto obtemos o email introducido no formulario, pero é o do tipo string e non me vale para obter o pk
      email_form_str = password_recovery_form_variable.cleaned_data.get('email')
      #Con esto obtemos o email introducido no formulario pero este é do tipo "registration.models.CustomUser" que me vale para obter o pk do email
      email_form =  CustomUser.objects.filter(email=email_form_str).first()
      user_name = CustomUser.objects.get(email = email_form).username
      if CustomUser.objects.filter(email=email_form).exists():
        #This is to generate a random token to include in the link which will be sent to the customer and he/she will be able to reset the password.
        token = str(uuid.uuid4())
        #Con esto codificamos o user_id (pk) correspondente ao email incluido no formulario
        uidb64=urlsafe_base64_encode(force_bytes(email_form.pk))
        #uid = request.user.id
        language = get_language()
        send_reset_password_mail (request, email_form, user_name, uidb64, token, language)
        messages.add_message(request, messages.SUCCESS, _('An email was sent to your email inbox'))
        return redirect('password_reset_done')
      else:
        messages.add_message(request, messages.ERROR, _('The email does not exist in our data base. Please, create a new account.'))
    else:
      for field, error in password_recovery_form_variable.errors.items():
        password_recovery_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
        messages.add_message(request, messages.ERROR, _('The email is not valid'))
        #Cando o formulario ten un erro temos que volver cargar o idioma que o pillamos da url, polo tanto esto ponme no formulario do idioma, o mesmo idioma que hai na url
        form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})

  context = {
    'form_language_html': form_language,
    'email_recovery' : password_recovery_form_variable,
  }
  return render (request, 'password_reset.html', context)

def password_reset_sent_view (request):
  #Formulario IDIOMA
  #Eiqui o que fago é coller o idioma da url que me ven a través do request.
  initial_language = request.LANGUAGE_CODE
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST)
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)

  context = {
      'form_language_html' : form_language,
  }
  return render (request, 'password_reset_sent.html', context)

#This is a function which renders the view of the Password Recovery when user has to introduce his/her new password. 
def password_new_password_view(request, uidb64, token):
  #Neste caso o que fago e coller o idioma do usuario, porque como xa teño na vista anterior introducín o email, a url que se envía no email para resetear o contrasinal
  #e que leva a esta vista, ten o email xa contido. Pois o que fago con ese email e ver o idioma que ten o usuario configurado para mostrarlle a páxina no idioma correcto.
  uid = force_str(urlsafe_base64_decode(uidb64))
  user = CustomUser.objects.get(pk=uid)
  user_language = CustomUser.objects.get(pk = uid).language
  initial_language = user_language
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST)
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)
      #Nesta sección o que fago e cambiar o idioma na url
      current_language = get_language()
      current_url = request.build_absolute_uri()
      new_url = re.sub(r'/[a-z]{2}/', f'/{current_language}/', current_url)
      return redirect(new_url)
    
  password_reset_form = password_new_form(user, data=request.POST)
  if request.method == 'POST' and not form_language.is_valid():
    if password_reset_form.is_valid():
      password_reset_form.save()
      #Ca conta do GoogleAuth tuven que por 2 backeds no settings file, con esto indico cal é o backend que
      #ten que utilizar cando se garden/cambien os atributos do personal data
      user.backend = 'django.contrib.auth.backends.ModelBackend'
      #Logeamos o usuario directamente
      login(request, user)
      #E activamos o idioma que ten o usuario configurado:
      user_language = CustomUser.objects.get(email = user).language
      activate(user_language)
      messages.add_message(request, messages.SUCCESS, _('Your password has been changed'))
      return redirect('bicleteiros_home_page')
    else:
      for field, error in password_reset_form.errors.items():
        password_reset_form[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
        messages.add_message(request, messages.ERROR, _("Check the below errors and try again!"))
        #Cando o formulario ten un erro temos que volver cargar o idioma que o pillamos da url, polo tanto esto ponme no formulario do idioma, o mesmo idioma que hai na url
        form_language = language_home_page_no_registration_form(initial={'language': request.LANGUAGE_CODE})

  context = {
    'form_language_html' : form_language,
    'reset_password_form' : password_reset_form
  }
  return render (request, 'password_reset_complete.html', context)


def email_visualization_password_recovery_view (request):
  #Collemos os valores que veñen a través da url
  email_user = request.GET.get('email', None)
  user_name = request.GET.get('username', None)
  uidb64_user = request.GET.get('uidb64_url', None)
  token_user =  request.GET.get('token_url', None)
  language_user = request.GET.get('language_url', None)
  current_site = get_current_site(request)
  password_recovery_link = f'http://{current_site}/{language_user}/password_recovery_update/{uidb64_user}/{token_user}/'

  context = {
    'username_html': user_name,
    'password_recovery_link_html': password_recovery_link
  }
  return render(request, 'email_body_password.html', context)


def privacy_policy_page_view (request):
  #Formulario IDIOMA
  #Eiqui o que fago é coller o idioma da url que me ven a través do request.
  initial_language = request.LANGUAGE_CODE
  #Esto ponme no formulario do idioma, co mesmo idioma que hai na url
  form_language = language_home_page_no_registration_form(initial={'language': initial_language})
  if request.method == 'POST':
    form_language = language_home_page_no_registration_form(data = request.POST)
    if form_language.is_valid():
      selected_language = form_language.cleaned_data['language']
      activate(selected_language)

  context = {
      'form_language_html' : form_language,
  }
  return render (request, 'privacy_policy_page.html', context)

#-------------------------------------ESTAS SON AS VIEWS DA CONFIGURACIÓN DO USUARIO--------------------------------------------------------

def delete_account_view (request):
  delete_account_form_variable = delete_account_form(data=request.POST)
  if request.method == 'POST':
    if delete_account_form_variable.is_valid():
      #Getting the text which have typed on the form.
      text_delete_form = delete_account_form_variable.cleaned_data.get('text_to_delete')
      #Getting the user which is logged
      current_user = CustomUser.objects.get(id=request.user.id)
      if str(text_delete_form) == str("terrameiga"):
        current_user.delete()
        messages.add_message(request, messages.SUCCESS, _('Your account has been deleted. We hope see you back soon!'))
        return redirect('home_page_no_registered')
      else:
        #Esto é para que se vacíe o formulario por se hai un erro
        delete_account_form_variable = delete_account_form()
        messages.add_message(request, messages.ERROR, _('Please, type "terrameiga". The text has to be lowercase and without quotes'))
    else:
      messages.add_message(request, messages.ERROR, _('Please, type "terrameiga". The text has to be lowercase and without quotes'))
  context = {
    'delete_form' : delete_account_form_variable
  }
  return render (request, 'profile_account/delete_account.html', context)

def personal_data_view(request):
  #Collemos a info do usuario que está logeado para pola no formulario
  current_user = CustomUser.objects.get(id=request.user.id)
  #Con esto ordenase a lista de country list en fucnión do idioma que está actualmente na sesión. Senon fago esto, por exemplo se teño a páxina en español os países estarían ordenados
  #basados no inglés e non no idioma que está activado na sesión
  sorted_country_list = sorted(country_list_values, key=lambda x: str(x[1]))
  #Neste caso, ao personal_data_form pasámoslle a info do user que será a que vaia a aparecer no formulario, e tamén definimos unha función en forms.py para pasarlle ao formulario
  #a sorted_country_list. A función está debaixo da clase "personal_data_form".
  form_personal_data = personal_data_form(request.POST or None, sorted_country_list=sorted_country_list, instance=current_user)
  if request.method == 'POST':
    if form_personal_data.is_valid():
      #Ca conta do GoogleAuth tuven que por 2 backeds no settings file, con esto indico cal é o backend que
      #ten que utilizar cando se garden/cambien os atributos do personal data
      current_user.backend = 'django.contrib.auth.backends.ModelBackend'
      form_personal_data.save()
      user_language = CustomUser.objects.get(email = current_user).language
      #Con esto activo o idioma que o usuario seleccionou no seu user_settings.
      activate(user_language)
      #Como o sistema me fai log_out, eu poño función para manter a sesión iniciada.
      login(request, current_user)
      messages.add_message(request, messages.SUCCESS, _("Your personal data has been updated"))
      return redirect('personal_data')
    else:
      for field, error in form_personal_data.errors.items():
          form_personal_data[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
      messages.add_message(request, messages.ERROR, _("The data could not be updated. Please check the below errors"))
  context = {
      'personal_data_update_form':form_personal_data
  }
  return render (request, 'profile_account/personal_data.html/', context)

def password_update_view(request):
  if request.method == 'POST':
    form_password_update = password_update_form(request.user, request.POST)
    if form_password_update.is_valid():
        user = form_password_update.save()
        # Importante
        update_session_auth_hash(request, user)
        messages.add_message(request, messages.SUCCESS, _("Your password has been updated!"))
        return redirect('password')
    else:
        # Eiqui o que fago e que recorra os distintos fields do form e que lle 
        # asigne o formato de error (O borde en vermello)
        for field, error in form_password_update.errors.items():
          form_password_update[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
          messages.add_message(request, messages.ERROR, _("Check the below errors and try again! If you signed up with GOOGLE, terrameiga.bike is not managing your password"))
  else:
        # If it's a GET request, create an empty form
        form_password_update = password_update_form(request.user)

  context = {
      'password_update_form': form_password_update
  }
  return render (request, 'profile_account/password_data.html', context)

    