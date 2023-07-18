from django.shortcuts import render, redirect
from registration.forms import sign_in_form_1, sign_up_form_2, personal_data_form, password_update_form, delete_account_form, password_reset_form, password_new_form
#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages
#Esto carga un formulario que xa está preconfigurado para a autentificación do usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
#Esto é para que cargue un paquete que autentifique (para ver se o usuario está xa rexistrado na nosa base de datos), para que logee o usuario por nós e para lle faga log out
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from .models import CustomUser
#This is to generate a random token which will be used in the url which will be sent to the email user to reset the password
import uuid
#Importamos un paquete para codificar o user_id (o pk) que vai na url que se lle envía ao usuario ao correo para resetear o contrasinal. O force bytes tamén e para codificar o pk
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .helpers import send_reset_password_mail, send_confirm_email

#Paquete para traducir texto que se xenera nas view. Neste caso é o texto das alertas
#from django.utils.translation import gettext as _
def index(request):
   #text = _("Esto é texto aleatorio")
   #return render(request, "home_page_castellano.html")
  context = {
    'texto': 'Hola'
  }
  return render(request, "templates/home_page_castellano.html", context)

def sign_up_view(request):
  # create a form instance and populate it with data from the request:
  sign_up_form_variable = sign_up_form_2(data=request.POST)
  if request.method == 'POST':
    if sign_up_form_variable.is_valid():
      user_name = sign_up_form_variable.cleaned_data.get('username')
      #Con esto obtemos o email introducido no formulario, pero é o do tipo string e non me vale para obter o pk
      email_form_str = sign_up_form_variable.cleaned_data.get('email')
      password_form = sign_up_form_variable.cleaned_data.get('password1')
      user = CustomUser.objects.create_user(user_name, email_form_str, password_form)
      #Con esto fago o usuario como non activo ata que confirme a súa conta de correo. Cando confime a conta o usario pasará a un estado de Activo.
      user.is_active = False
      user.save()
      #Con esto obtemos o email introducido no formulario pero este é do tipo "registration.models.CustomUser" que me vale para obter o pk do email
      email_form =  CustomUser.objects.filter(email=email_form_str).first()
      #This is to generate a random token to include in the link which will be sent to the customer and he/she will be able to reset the password.
      token = str(uuid.uuid4())
      #Con esto codificamos o user_id (pk) correspondente ao email incluido no formulario
      uidb64=urlsafe_base64_encode(force_bytes(email_form.pk))
      send_confirm_email (email_form, uidb64, token)
      #Esto é para que me mostre a mensaxe de que se fixo log-in correctamente
      messages.add_message(request, messages.SUCCESS,
                          """
                          <h2> Please, go to your email and verify your account</h2>
                            <p>
                             Welcome, you will enjoy the latest news about cycling and interesting items
                             for your bike
                            </p>
                          """  + user_name)
      return redirect('account_confirmation_email_sent')
    else:
      # Eiqui o que fago e que recorra os distintos fields do form e que lle 
      # asigne o formato de error (O borde en vermello)
       for field, error in sign_up_form_variable.errors.items():
          sign_up_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
          #Solo me interesa o error, e eiqui é o que estou collerndo, a frase dos errores
          messages.add_message(request, messages.WARNING, error)
       
  context = {
        'sign_up_form':sign_up_form_variable
  }
  return render (request, '2_sign_up.html', context)

def sign_up_email_validation_confirmation_view (request, uidb64, token):
  uid = force_str(urlsafe_base64_decode(uidb64))
  user = CustomUser.objects.get(pk=uid)
  #Unha vez que clicka no link para verificar a súa conta, nos activamos o seu email.
  user.is_active = True
  user.save()
  #NOTA interesante. Se queres coller algún atributo do usuario bastaría con escribir "user.password" ou "user.name"....
  #Con esta función fago log-in sen necesidade de introducir a contraseña. Ten en conta que eu nesta función non teño contraseña porque Django encríptaa e
  # non hai forma de desencriptala
  login(request, user)
  return redirect('personal_data')

def log_out_view (request):
   logout(request)
   messages.add_message(request, messages.INFO, "You have been logged out!")
   return redirect('home_page')

# Create your views here.
def sign_in_view(request):
  # If this is a POST request we need to process the form data (Todos os log-in dos clientes que nos cheguen serán POST)
  sign_in_form_variable = sign_in_form_1(request, data=request.POST)
  if request.method == 'POST':
    if sign_in_form_variable.is_valid():
      #Non entendo mui ben porque para coller o email teño que collelo do username no form, pero ten que ser así para que funcione.
      email_form = sign_in_form_variable.cleaned_data.get('username')
      password_form = sign_in_form_variable.cleaned_data.get('password')
      #Authenticate user returns the email of the user
      user_auth = authenticate(request, email=email_form, password=password_form)
      if user_auth is not None:
        login(request, user_auth)
        messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            Eiqui metes o que quieras
                        </p>
                        """
                    )
        return redirect('personal_data')
    else:
      for field, error in sign_in_form_variable.errors.items():
        # Eiqui o que fago e que recorra os distintos fields do form e que lle 
      # asigne o formato de error (O borde en vermello)
        sign_in_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
      # Solo me interesa o error, e eiqui é o que estou collerndo, a frase dos errores
        messages.add_message(request, messages.WARNING, error)
      return redirect('sign_in')
  context = {
        "sign_in_form": sign_in_form_variable
  }
  return render (request, '1_sign_in.html', context)

def personal_data_view(request):
  #Collemos a info do usuario que está logeado para pola no formulario
  current_user = CustomUser.objects.get(id=request.user.id)
  #Neste caso, ao personal_data_form pasámoslle a info do user que será a que vaia a aparecer no formulario
  form_personal_data = personal_data_form(request.POST or None, instance=current_user)
  if request.method == 'POST':
    if form_personal_data.is_valid():
      form_personal_data.save()
      #Como o sistema me fai log_out, eu poño función para manter a sesión iniciada.
      login(request, current_user)
      messages.add_message(request, messages.SUCCESS, 'Your personal data has been updated')
      return redirect('personal_data')
    else:
      messages.add_message(request, messages.WARNING, 'os datos non se puderon actualizar')
  context = {
      'personal_data_update_form':form_personal_data
  }
  return render (request, 'profile_account/personal_data.html/', context)

def password_update_view(request):
  form_password_update = password_update_form(request.user, request.POST)
  if request.method == 'POST':
    if form_password_update.is_valid():
        user = form_password_update.save()
        # Importante
        update_session_auth_hash(request, user)
        messages.add_message(request, messages.SUCCESS, 'Your password has been updated')
        return redirect('password')
    else:
        messages.add_message(request, messages.WARNING, 'The password could not be updated')
  context = {
      'password_update_form': form_password_update
  }
  return render (request, 'profile_account/password_data.html', context)


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
        messages.add_message(request, messages.SUCCESS, 'Your account has been deleted')
        return redirect('home_page')
      else:
        #Esto é para que se vacíe o formulario por se hai un erro
        delete_account_form_variable = delete_account_form()
        messages.add_message(request, messages.SUCCESS, 'Please type "terrameiga"')
    else:
      messages.add_message(request, messages.SUCCESS, 'The form is not valid')
  context = {
    'delete_form' : delete_account_form_variable
  }
  return render (request, 'profile_account/delete_account.html', context)

      

def password_reset_view(request):
  password_recovery_form_variable = password_reset_form (data=request.POST)
  uid = request.user.id
  print(uid)
  if request.method == "POST":
    if password_recovery_form_variable.is_valid():
      #Con esto obtemos o email introducido no formulario, pero é o do tipo string e non me vale para obter o pk
      email_form_str = password_recovery_form_variable.cleaned_data.get('email')
      #Con esto obtemos o email introducido no formulario pero este é do tipo "registration.models.CustomUser" que me vale para obter o pk do email
      email_form =  CustomUser.objects.filter(email=email_form_str).first()
      if CustomUser.objects.filter(email=email_form).exists():
        print('existe')
        #This is to generate a random token to include in the link which will be sent to the customer and he/she will be able to reset the password.
        token = str(uuid.uuid4())
        #Con esto codificamos o user_id (pk) correspondente ao email incluido no formulario
        uidb64=urlsafe_base64_encode(force_bytes(email_form.pk))
        print(uidb64)
        #uid = request.user.id
        #print(uid)
        send_reset_password_mail ( email_form, uidb64, token)
        messages.add_message(request, messages.SUCCESS, 'An email was sent to your email inbox')
        return redirect('password_reset_done')
      else:
        messages.add_message(request, messages.WARNING, 'The email does not exist in our data base')
    else:
      messages.add_message(request, messages.WARNING, 'Email not valid')

  context = {
    'email_recovery' : password_recovery_form_variable
  }
  return render (request, 'password_reset.html', context)


def password_new_password_view(request, uidb64, token):
  uid = force_str(urlsafe_base64_decode(uidb64))
  user = CustomUser.objects.get(pk=uid)
  password_reset_form = password_new_form(user, data=request.POST)
  if request.method == 'POST':
    if password_reset_form.is_valid():
      password_reset_form.save()
      messages.add_message(request, messages.SUCCESS, 'Your password has been reseted with your email')
      return redirect('sign_in')
    else:
      messages.add_message(request, messages.WARNING, "The password is not maching or the link is not valid anymore")

  context = {
    'reset_password_form' : password_reset_form
  }
  return render (request, 'password_reset_confirm.html', context)


def profile_account(request):
  # create a form instance and populate it with data from the request:
  return render (request, 'profile_account.html')
    