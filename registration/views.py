from django.shortcuts import render, redirect
from registration.forms import registration_form_1
#, registration_form_2, registration_form_3
#Este paquete é para mostrar as alertas (mensaxes) unha vez se completa un campo como é debido.
from django.contrib import messages

# Create your views here.
def registration_view_1(request):
  # create a form instance and populate it with data from the request:
  registration_form_variable = registration_form_1(data=request.POST)
  # if this is a POST request we need to process the form data (Todos os registros dos corredores que nos cheguen serán POST)
  if request.method == 'POST':
    # check whether it's valid:
    if registration_form_variable.is_valid():
      # Create registration object but don't save to database yet
      new_registration_form_variable = registration_form_variable.save(commit=False)
      # Save the registration to the database
      new_registration_form_variable.save()
      #Esto é para que me mostre a mensaxe de que se gardou/enviou o rexistro do corredor
      messages.success(request, 'Graciñas por subscribirte a nosa newletter. Non seremos moi pesados.')
      #registration_2 e para que se todo vai ben, vaia ao 2º step do rexistro. Vaste as url e colles a url que queres que che retorne
      return redirect('home_page_gl')
    else:
      # Eiqui o que fago e que recorra os distintos fields do form e que lle 
      # asigne o formato de error (O borde en vermello)
      for field, errors in registration_form_variable.errors.items():
          registration_form_variable[field].field.widget.attrs.update({'style': 'border-color:red; border-width: medium'})
          print (errors)
      #Esto imprime o error xusto debaixo do cajetín que conten o erro
      messages.error(request, registration_form_variable.errors)
      #messages.error(request, "Insira un enderezo de correo electrónico válido!")
      print(registration_form_variable.errors)
 
  context = {
        'form_1':registration_form_variable
  }
  return render (request, 'registration_1_gl.html', context)


# def registration_view_2(request):
#   # create a form instance and populate it with data from the request:
#   registration_form_variable = registration_form_2(data=request.POST)
 
#   context = {
#         'form_2':registration_form_variable
#   }
#   return render (request, 'registration_2_gl.html', context)

# def registration_view_3(request):
#     # create a form instance and populate it with data from the request:
#     registration_form_variable = registration_form_3(data=request.POST)

#     context = {
#         'form_3':registration_form_variable
#     }
#     return render (request, 'registration_3_gl.html', context)
    