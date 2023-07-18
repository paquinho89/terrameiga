from django.shortcuts import render, redirect

# Create your views here.
from newsletter.forms import form_newsletter

#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages

# Create your views here.

# Create your views here.
#NOTA: Para subscribirse a newsletter non vou a pedir a autentificación do email porque é algo que o usuario proactivamente quere recibir e entendo que meterá un
# correo válido
def newsletter_home_page_view(request):
  # create a form instance and populate it with data from the request:
  newsletter_email = form_newsletter(data=request.POST)
  # if this is a POST request we need to process the form data (Todos os comentarions que nos cheguen serán POST)
  if request.method == 'POST':
    # check whether it's valid:
    if newsletter_email.is_valid():
      new_subscriber_email = newsletter_email.save(commit=False)
      new_subscriber_email.save()
      
      messages.success(request, 'Thanks for subscribing to our newsletter. No worries, we will not send you a lot of emails')
      return redirect('home_page')

    # if a GET (or any other method) we'll create a blank form
    else:
      #Comentando a seguinte línea o formulario non se vacía despois do error. 
      #newsletter_email = form_newsletter()
      # Eiqui o que fago e que recorra os distintos fields do form ("neste caso solo un") e que lle 
      # asigne o formato de error (O borde en vermello)
      for field, errors in newsletter_email.errors.items():
        newsletter_email[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
      #Esto imprime o error xusto debaixo do cajetín para inserir o correo
      messages.error(request, newsletter_email.errors)
      #messages.error(request, "Insira un enderezo de correo electrónico válido!")
        
  context = {
        'form_newsletter_home_page':newsletter_email,
  }

  return render (request, 'templates/home_page.html', context)
