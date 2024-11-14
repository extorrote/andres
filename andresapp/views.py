from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Agente, Venta, Alquiler, Terreno, PreConstruccion
from .forms import AgenteForm, VentaForm, AlquilerForm, TerrenoForm, PreConstruccionForm
from django.shortcuts import get_object_or_404, render
from datetime import datetime
# View to create an agent
def create_agent(request):
    if request.method == 'POST':
        form = AgenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agent created successfully!')
            return redirect('create_agent')
    else:
        form = AgenteForm()
    return render(request, 'create_agent.html', {'form': form})

# View to create a property (Ventas)
def create_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST, request.FILES)  # Ensure request.FILES is included
        if form.is_valid():
            form.save()
            messages.success(request, 'Property created successfully!')
            return redirect('create_venta')
        else:
            print(form.errors)  # Debugging: Check form errors
    else:
        form = VentaForm()
    return render(request, 'create_venta.html', {'form': form})



from django.conf import settings
def lista_ventas(request):
    propiedades = Venta.objects.all()  # Fetch all properties for sale
    default_image_url = f"{settings.STATIC_URL}default_image.jpg"  # Adjust path as needed, ESTO SE AGREGO PARA PODER ABRIR LA IMAGEN EN FULL SCREEN EN LA TEMPLATE 
    return render(request, 'index.html', {'propiedades': propiedades, 'default_image_url': default_image_url})



def detalle_venta(request, pk):
    propiedad = get_object_or_404(Venta, pk=pk)
    return render(request, 'detalle_venta.html', {'propiedad': propiedad})


def create_alquiler(request):
    if request.method == 'POST':
        form = AlquilerForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Rental property created successfully!')
            return redirect('create_alquiler')
    else:
        form = AlquilerForm()
    return render(request, 'create_alquiler.html', {'form': form})


def alquiler_list(request):
    alquileres = Alquiler.objects.all()  # Get all rental properties
    return render(request, 'alquiler_list.html', {'alquileres': alquileres})

def detalle_alquiler(request, pk):
    alquiler = get_object_or_404(Alquiler, pk=pk)  # Fetch the rental property or return a 404 if not found
    return render(request, 'alquiler_detail.html', {'alquiler': alquiler})



# View to create a property (Terreno)
def create_terreno(request):
    if request.method == 'POST':
        form = TerrenoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Land property created successfully!')
            return redirect('create_terreno')
    else:
        form = TerrenoForm()
    return render(request, 'create_terreno.html', {'form': form})

def terrenos_list(request):
    terrenos = Terreno.objects.all()  # Get all rental properties
    return render(request, 'terrenos_list.html', {'terrenos': terrenos})







def terrenos_detail(request, pk):
    terreno = get_object_or_404(Terreno, pk=pk)  # Ensure you're querying the Terreno model
    return render(request, 'terreno_detail.html', {'terreno': terreno})

# View to create a property (PreConstruccion)
def create_pre_construccion(request):
    if request.method == 'POST':
        form = PreConstruccionForm(request.POST, request.FILES)  # Make sure to include request.FILES for image uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Pre-construction property created successfully!')
            return redirect('pre_construccion_list')  # Change to redirect to the list or detail view
        else:
            # Handle form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = PreConstruccionForm()
    
    return render(request, 'create_pre_construccion.html', {'form': form})



def pre_construccion_list(request):
    pre_construcciones = PreConstruccion.objects.all()  # Get all pre-construction properties
    return render(request, 'pre_construccion_list.html', {'pre_construcciones': pre_construcciones})


def pre_construccion_detail(request, pk):
    pre_construccion = get_object_or_404(PreConstruccion, pk=pk)  # Fetch the specific PreConstruccion
    return render(request, 'pre_construccion_detail.html', {'pre_construccion': pre_construccion})





def privacy_policy(request):
    current_year = datetime.now().year
    return render(request, 'privacy_policy.html', {'current_year': current_year})


def terms_of_service(request):
    return render(request, 'terms_of_service.html')


def about_us(request):
    return render (request, 'about_us.html')

from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages


from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # Define a list of recipient emails
            recipient_list = ['andrew_2000m@hotmail.com', 'casapv.com@gmail.com', 'wwwstephen95live@gmail.com', 'normamontiel05@hotmail.com']

            # Create the email subject
            subject = f'Contact Form Submission from {name}'

            # Create the HTML message
            html_message = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 20px;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: auto;
                        background: #D99F59; /* Main color */
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #ffffff; /* White text for contrast */
                    }}
                    p {{
                        font-size: 16px;
                        color: #333; /* Dark text for readability */
                    }}
                    .footer {{
                        margin-top: 20px;
                        font-size: 14px;
                        text-align: center;
                        color: #ffffff; /* White footer text */
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Hemos Recibido tu Mensaje!</h1>
                    <p><strong>Nombre:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Teléfono:</strong> {phone}</p>
                    <p><strong>Mensaje:</strong></p>
                    <p>{message}</p>
                    <div class="footer">
                        <p>Gracias por Contactar www.casapv.com, en breve te Contactará uno de Nuestros Agentes.</p>
                    </div>
                </div>
            </body>
            </html>
            """

            # Create and send the email
            email = EmailMultiAlternatives(subject, strip_tags(html_message), 'casapv.com@gmail.com', recipient_list)
            email.attach_alternative(html_message, "text/html")
            email.send(fail_silently=False)

            messages.success(request, '¡Gracias por Contactarnos! Su mensaje ha sido Enviado.')
            return redirect('lista_ventas')
    else:
        form = ContactForm()

    return render(request, 'lista_ventas.html', {'form': form})





from django.db.models import Q
from rest_framework import generics
from .models import Venta
from .serializers import VentaSerializer

# andresapp/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Venta
from .serializers import VentaSerializer

@api_view(['GET'])
def Buscador_Ventas(request):
    # Get the search parameters from the request
    colonia = request.GET.get('colonia', '')
    habitaciones = request.GET.get('habitaciones', '')
    baños = request.GET.get('baños', '')
    precio = request.GET.get('precio', '')

    # Build the search query
    query = Q()

    if colonia:
        query &= Q(colonia__icontains=colonia)
    if habitaciones:
        query &= Q(habitaciones__icontains=habitaciones)
    if baños:
        query &= Q(baños__icontains=baños)
    if precio:
        query &= Q(precio__icontains=precio)

    # Filter the properties based on the search query
    properties = Venta.objects.filter(query)

    # Use the VentaSerializer to serialize the properties and include the detail_url
    serializer = VentaSerializer(properties, many=True)

    # Return the serialized data as a JSON response
    return Response({'properties': serializer.data})

    





from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Alquiler
from .serializers import AlquilerSerializer

@api_view(['GET'])
def Buscador_Alquiler(request):
    # Get the search parameters from the request
    colonia = request.GET.get('colonia', '')
    habitaciones = request.GET.get('habitaciones', '')
    baños = request.GET.get('baños', '')
    precio = request.GET.get('precio', '')

    print("Received parameters:", colonia, habitaciones, baños, precio)  # Debug print

    # Build the search query
    query = Q()

    if colonia:
        query &= Q(colonia__icontains=colonia)
    if habitaciones:
        query &= Q(habitaciones__icontains=habitaciones)
    if baños:
        query &= Q(baños__icontains=baños)
    if precio:
        query &= Q(precio__lte=precio)  # Assuming you want to filter for properties <= precio

    # Filter the properties based on the search query
    properties = Alquiler.objects.filter(query)

    # Debug the query
    print("Filtered properties:", properties)  # Debug print

    # Serialize the filtered properties
    serializer = AlquilerSerializer(properties, many=True)

    # Return the filtered data as a JSON response
    return JsonResponse({'properties': serializer.data})

    
    

from .serializers import TerrenoSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Terreno
from .serializers import TerrenoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.http import JsonResponse
from .models import Terreno
from .serializers import TerrenoSerializer

@api_view(['GET'])
def Buscador_Terreno(request):
    # Get the search parameters from the request
    ubicacion = request.GET.get('ubicacion', '')
    precio = request.GET.get('precio', '')  # Replace 'precio_preventa' with 'precio'
    
    # Debug print to see the received parameters
    print("Received parameters:", ubicacion, precio)  

    # Build the search query
    query = Q()

    if ubicacion:
        query &= Q(ubicacion__icontains=ubicacion)  # Case-insensitive search for location

    if precio:
        try:
            precio = float(precio)  # Convert 'precio' to float
            query &= Q(precio__lte=precio)  # Filter terrenos with precio <= provided price
        except ValueError:
            return JsonResponse({'error': 'Invalid price format'}, status=400)

    # You can add more conditions here for other fields like area, tipo, etc.

    # Filter the terrenos based on the search query
    terrenos = Terreno.objects.filter(query)

    # Debug the filtered results
    print("Filtered terrenos:", terrenos)  

    # Serialize the filtered terrenos
    serializer = TerrenoSerializer(terrenos, many=True)

    # Return the filtered data as a JSON response
    return JsonResponse({'terrenos': serializer.data})





from .serializers import  PreVentasSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import PreConstruccion  # Make sure this is the correct model
from .serializers import PreVentasSerializer  # Import the updated serializer

from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PreConstruccion
from .serializers import PreVentasSerializer

@api_view(['GET'])
def Buscador_pre_ventas(request):
    # Get the search parameters from the request
    ubicacion = request.GET.get('ubicacion', '')
    precio_preventa = request.GET.get('precio_preventa', '')
    tipo_de_proyecto = request.GET.get('tipo_de_proyecto', '')
    habitaciones = request.GET.get('habitaciones', '')

    # Build the search query using Q objects
    query = Q()

    if ubicacion:
        query &= Q(ubicacion__icontains=ubicacion)  # Case-insensitive search for 'ubicacion'
    if precio_preventa:
        query &= Q(precio_preventa__icontains=precio_preventa)  # Assuming 'precio_preventa' is numeric or string
    if tipo_de_proyecto:
        query &= Q(tipo_de_proyecto__icontains=tipo_de_proyecto)  # Filter by project type
    if habitaciones:
        query &= Q(habitaciones__icontains=habitaciones)  # Filter by number of rooms (assuming it's a string or number)

    # Filter the PreConstruccion objects based on the query
    properties = PreConstruccion.objects.filter(query)

    # Serialize the filtered properties
    serializer = PreVentasSerializer(properties, many=True)

    # Return the serialized data as a JSON response
    return Response({'properties': serializer.data})


    
    
    
    
    
from django.shortcuts import render, redirect
from .forms import PerfilamientoForm

def crear_perfilamiento(request):
    if request.method == 'POST':
        form = PerfilamientoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('perfilamiento_list')  # Replace with your success URL
    else:
        form = PerfilamientoForm()
    
    return render(request, 'crear_perfilamiento.html', {'form': form})


from django.shortcuts import render
from .models import Perfilamiento

def perfilamiento_list(request):
    perfilamientos = Perfilamiento.objects.all()
    return render(request, 'lista_perfilamientos.html', {'perfilamientos': perfilamientos})



from django.shortcuts import get_object_or_404

def editar_perfilamiento(request, pk):
    perfilamiento = get_object_or_404(Perfilamiento, pk=pk)
    if request.method == 'POST':
        form = PerfilamientoForm(request.POST,request.FILES, instance=perfilamiento)
        if form.is_valid():
            form.save()
            return redirect('perfilamiento_list')  # Redirect to the list view after saving
    else:
        form = PerfilamientoForm(instance=perfilamiento)
    
    return render(request, 'editar_perfilamiento.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import FichaTecnicaForm



def crear_ficha_tecnica(request):
    if request.method == 'POST':
        form = FichaTecnicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_fichas_tecnicas')  # Redirige a una página de éxito o lista de fichas
    else:
        form = FichaTecnicaForm()
    
    return render(request, 'crear_ficha_tecnica.html', {'form': form})




from django.shortcuts import render
from .models import FichaTecnica

def lista_fichas_tecnicas(request):
    fichas = FichaTecnica.objects.all()  # Obtiene todas las fichas técnicas
    return render(request, 'lista_fichas_tecnicas.html', {'fichas': fichas})

def editar_ficha_tecnica(request, pk):
    ficha = get_object_or_404(FichaTecnica, pk=pk)
    if request.method == 'POST':
        form = FichaTecnicaForm(request.POST, request.FILES, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('lista_fichas_tecnicas')  # Redirect to the list view after saving
    else:
        form = FichaTecnicaForm(instance=ficha)
    
    return render(request, 'editar_ficha_tecnica.html', {'form': form})



def ultimo_documento(request):
    return render(request,'ultimo_documento.html')



from django.shortcuts import render, redirect
from .forms import InfoExtraForm

def create_info_extra(request):
    if request.method == 'POST':
        form = InfoExtraForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_levantamientos')  # Replace with your success URL or view
    else:
        form = InfoExtraForm()

    return render(request, 'crear_levantamiento.html', {'form': form})


from django.shortcuts import render
from .models import InfoExtra

def list_info_extra(request):
    info_list = InfoExtra.objects.all()  # Retrieve all InfoExtra instances
    return render(request, 'lista_levantamientos.html', {'info_list': info_list})


def editar_levantamiento(request, pk):
    # Retrieve the InfoExtra instance to be edited
    info_extra = get_object_or_404(InfoExtra, pk=pk)

    if request.method == 'POST':
        form = InfoExtraForm(request.POST, request.FILES, instance=info_extra)  # Prefill form with the instance data
        if form.is_valid():
            form.save()  # Save the changes to the database
            return redirect('lista_levantamientos')  # Redirect to the list view after saving
    else:
        form = InfoExtraForm(instance=info_extra)  # Prefill form with instance data if GET request

    return render(request, 'editar_levantamiento.html', {'form': form, 'info_extra': info_extra})


from django.contrib.auth import authenticate,login,logout
def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')#ESTO ES LO QUE LE HE PUESTO EN EL NAME EN EL CAMPO DEL FORMULARIO
        user=authenticate(request,username=username,password=password)#KEYBOL ARGUMENT ES CUANDO VA UN LA PRIMERA ES LA KEIBOLNAME  NOMBRE=NOMBRE LA SEGUNDA ES LA VARIABLE QUE ESTA RECIBIENDO
        if user is not None:
            login(request,user)
            return redirect('lista_ventas')
        else:
            messages.warning (request,'No te has identificado Correctamente')   


    return render (request,'login.html',{'title':'identificate'})


def logout_user(request):
    logout(request)
    return redirect ('lista_ventas')