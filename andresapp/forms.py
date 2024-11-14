from django import forms
from .models import Agente, Venta, Alquiler, Terreno, PreConstruccion

class AgenteForm(forms.ModelForm):
    class Meta:
        model = Agente
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'foto': 'Foto',
            'años_de_experiencia': 'Años de Experiencia',
        }

from django import forms
from .models import Agente, Venta

from django import forms
from .models import Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        labels = {
            'colonia': 'Colonia',
            'precio': 'Precio',
            'tipo_de_propiedad': 'Tipo de Propiedad',
            'medidas_de_la_propiedad': 'Superficie del Terreno',
            'cocina':'Cocina',
            'jardin':'jardin',
            'comedor':'Comedor',
            'balcon':'Balcon',
            'habitaciones': 'Habitaciones',
            'baños': 'Baños',
            'cuarto_de_servicio': 'Cuarto De Servicio',
            'sala': 'Sala',
            'piscina': 'Alberca',
            'numero_de_piso': 'Número de Piso',
            'amoblado': 'Amueblado',
            'privada_o_con_escrituras': 'Escrituras',
            'electrodomesticos_y_muebles_en_general': 'Electrodomésticos y Muebles en General',
            'paredes': 'Paredes',
            'tipo_de_calle': 'Tipo de Calle',
            'tipo_de_electricidad': 'Tipo de Electricidad',
            'informacion_extra': 'Información Extra',
            'comodidades_en_areas_comunes': 'Amenidades en Áreas Comunes',
            'elevador': 'Elevador',
            'rooftop': 'Rooftop',
            'gym': 'Gym',
            'estasionamiento': 'Estacionamiento',
            'condiciones_de_la_propiedad': 'Condiciones de la Propiedad',
            'pet_friendly': 'Pet Friendly',
            'vista_primaria': 'Vista Primaria',
            'vista_secundaria': 'Vista Secundaria',
            'imagen1': 'Imagen 1',
            'imagen2': 'Imagen 2',
            'imagen3': 'Imagen 3',
            'imagen4': 'Imagen 4',
            'imagen5': 'Imagen 5',
            'imagen6': 'Imagen 6',
            'imagen7': 'Imagen 7',
            'imagen8': 'Imagen 8',
            'imagen9': 'Imagen 9',
            'imagen10': 'Imagen 10',
            'imagen11': 'Imagen 11',
            'imagen12': 'Imagen 12',
            'imagen13': 'Imagen 13',
            'imagen14': 'Imagen 14',
            'imagen15': 'Imagen 15',
            'imagen16': 'Imagen 16',
            'youtube_link': 'Link de YouTube (Iframe)',
            'agua': 'Agua',
            'tipo_tipo_de_estufa': 'Tipo de Estufa',
            'aire_acondicionado': 'Aire Acondicionado',
            'calentador_de_agua': 'Calentador de Agua',
            'pago_de_mantenimiento': 'Pago de Mantenimiento',
            'que_incluye_el_pago_de_mantenimiento': 'Qué Incluye el Pago de Mantenimiento',
            'direccion_exacta': 'Dirección Exacta',
            'link_de_google_maps': 'Link de Google Maps (Iframe)',
            'agente': 'Agente',
        }

    def clean_youtube_link(self):
        link = self.cleaned_data.get('youtube_link')
        if link and (not link.startswith('<iframe') or 'youtube.com' not in link):
            raise forms.ValidationError('Invalid YouTube iframe link.')
        return link

    def clean_link_de_google_maps(self):
        link = self.cleaned_data.get('link_de_google_maps')
        if link and 'https://www.google.com/maps' not in link:
            raise forms.ValidationError('Invalid Google Maps link.')
        return link




from django import forms
from .models import Alquiler

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = '__all__'
        labels = {
            'colonia': 'Colonia',
            'precio': 'Precio',
            'habitaciones': 'Habitaciones',
            'baños': 'Baños',
            'sala': 'Sala',
            'cuarto_de_servicio': 'Cuarto De Servicio',
            'cocina':'Cocina',
            'jardin':'jardin',
            'comedor':'Comedor',
            'balcon':'Balcon',
            'tipo_de_propiedad': 'Tipo de Propiedad',
            'vista_primaria':'Vista Primaria',
            'vista_secundaria':'Vista Secundaria',
            'numero_de_piso': 'Número de Piso',
            'amoblado': 'Amueblado',
            'elevador': 'Elevador',
            'rooftop': 'Rooftop',
            'gym': 'Gym',
            'estasionamiento': 'Estacionamiento',
            'electrodomesticos_y_muebles_en_general': 'Electrodomésticos y Muebles en General',
            'condiciones_de_la_propiedad': 'Estado de la Propiedad',
            'tipo_de_electricidad': 'Tipo de Electricidad',
            'medidas_de_la_propiedad': 'Medidas de la Propiedad',
            'requisitos': 'Requisitos',
            'duracion_contrato': 'Duración del Contrato',
            'deposito': 'Depósito',
            'areas_comunes': 'Áreas Comunes',
            'piscina': 'Alberca',
            'pet_friendly': 'Pet Friendly',
            'tipo_tipo_de_estufa': 'Tipo de Estufa',
            'aire_acondicionado': 'Aire Acondicionado',
            'calentador_de_agua': 'Calentador de Agua',
            'pago_de_mantenimiento': 'Pago de Mantenimiento',
            'que_incluye_el_pago_de_mantenimiento': 'Qué Incluye el Pago de Mantenimiento',
            'informacion_extra': 'Información Extra',
            'direccion_exacta': 'Dirección Exacta',
            'created': 'Fecha de Creación',
            'updated': 'Fecha de Actualización',
            'imagen1': 'Imagen 1',
            'imagen2': 'Imagen 2',
            'imagen3': 'Imagen 3',
            'imagen4': 'Imagen 4',
            'imagen5': 'Imagen 5',
            'imagen6': 'Imagen 6',
            'imagen7': 'Imagen 7',
            'imagen8': 'Imagen 8',
            'imagen9': 'Imagen 9',
            'imagen10': 'Imagen 10',
            'imagen11': 'Imagen 11',
            'imagen12': 'Imagen 12',
            'imagen13': 'Imagen 13',
            'imagen14': 'Imagen 14',
            'imagen15': 'Imagen 15',
            'imagen16': 'Imagen 16',
            'youtube_link': 'Link de YouTube (Iframe)',
            'link_de_google_maps': 'Link de Google Maps (Iframe)',
            'agente': 'Agente',
        }

    def clean_youtube_link(self):
        link = self.cleaned_data.get('youtube_link')
        if not link.startswith('<iframe') or 'youtube.com' not in link:
            raise forms.ValidationError('Invalid YouTube iframe link.')
        return link

    def clean_link_de_google_maps(self):
        link = self.cleaned_data.get('link_de_google_maps')
        if 'https://www.google.com/maps' not in link:
            raise forms.ValidationError('Invalid Google Maps link.')
        return link

class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = '__all__'
        labels = {
            'ubicacion': 'Ubicación',
            'precio': 'Precio',
            'medidas': 'Medidas',
            'propiedad_privada_o_con_escrituras': 'Ejidal O Escrituras',
            'metros_cuadrados':'Metros Cuadrados',
            'uso_de_suelo': 'Uso de Suelo',
            'informacion_extra': 'Información Extra',
            'link_de_google_maps': 'Link de Google Maps (Iframe)',
            'direccion_exacta': 'Dirección Exacta',
            'created': 'Fecha de Creación',
            'updated': 'Fecha de Actualización',
            'imagen1': 'Imagen 1',
            'imagen2': 'Imagen 2',
            'imagen3': 'Imagen 3',
            'imagen4': 'Imagen 4',
            'imagen5': 'Imagen 5',
            'imagen6': 'Imagen 6',
            'imagen7': 'Imagen 7',
            'imagen8': 'Imagen 8',
            'youtube_link': 'Link de YouTube (Iframe)',
            'agente': 'Agente',
        }

    def clean_youtube_link(self):
        link = self.cleaned_data.get('youtube_link')
        if not link.startswith('<iframe') or 'youtube.com' not in link:
            raise forms.ValidationError('Invalid YouTube iframe link.')
        return link

    def clean_link_de_google_maps(self):
        link = self.cleaned_data.get('link_de_google_maps')
        if 'https://www.google.com/maps' not in link:
            raise forms.ValidationError('Invalid Google Maps link.')
        return link

from django import forms
from .models import PreConstruccion

class PreConstruccionForm(forms.ModelForm):
    class Meta:
        model = PreConstruccion
        fields = '__all__'
        labels = {
            'ubicacion': 'Ubicación',
            'precio_normal': 'Precio Normal',
            'precio_preventa': 'Precio Preventa',
            'anticipo': 'Anticipo (Enganche)',
            'tipo_de_proyecto': 'Tipo de Proyecto',
            'habitaciones': 'Habitaciones',
            'baños': 'Baños',
            'sala': 'Sala',
            'cocina':'Cocina',
            'jardin':'jardin',
            'comedor':'Comedor',
            'balcon':'Balcon',
            'cuarto_de_servicio': 'Cuarto De Servicio',
            'fecha_entrega': 'Fecha de Entrega',           
            'se_entrega_con': 'Se Entrega Con',
            'areas_comunes': 'Áreas Comunes',
            'piscina': 'Alberca',
            'numero_de_departamento': 'Número de departamento',
            'elevador': 'Elevador',
            'rooftop': 'Rooftop',
            'gym': 'Gym',
            'estasionamiento': 'Estacionamiento',
            'electrodomesticos_y_muebles_en_general': 'Electrodomésticos y Muebles en General',
            'agua': 'Agua',
            'amoblado': 'Amueblado',
            'paredes': 'Paredes',
            'tipo_de_calle': 'Tipo de Calle',
            'tipo_de_electricidad': 'Tipo de Electricidad',
            'comodidades_en_areas_comunes': 'Amenidades en Áreas Comunes',
            'aire_acondicionado': 'Aire Acondicionado',
            'calentador_de_agua': 'Calentador de Agua',
            'informacion_extra': 'Información Extra',
            'link_de_google_maps': 'Link de Google Maps (Iframe)',
            'direccion_exacta': 'Dirección Exacta',
            'medidas': 'Medidas',
            'metros_cuadrados': 'Metros Cuadrados',
            'politicas_de_venta':'Policicas de Venta',
            'escrituras':'Escrituras',
            'imagen1': 'Imagen 1',
            'imagen2': 'Imagen 2',
            'imagen3': 'Imagen 3',
            'imagen4': 'Imagen 4',
            'imagen5': 'Imagen 5',
            'imagen6': 'Imagen 6',
            'imagen7': 'Imagen 7',
            'imagen8': 'Imagen 8',
            'imagen9': 'Imagen 9',
            'imagen10': 'Imagen 10',
            'imagen11': 'Imagen 11',
            'imagen12': 'Imagen 12',
            'imagen13': 'Imagen 13',
            'imagen14': 'Imagen 14',
            'imagen15': 'Imagen 15',
            'imagen16': 'Imagen 16',
            'youtube_link': 'Link de YouTube (Iframe)',
            'agente': 'Agente',
        }
        

    def clean_youtube_link(self):
        link = self.cleaned_data.get('youtube_link')
        if not link.startswith('<iframe') or 'youtube.com' not in link:
            raise forms.ValidationError('Invalid YouTube iframe link.')
        return link

    def clean_link_de_google_maps(self):
        link = self.cleaned_data.get('link_de_google_maps')
        if 'https://www.google.com/maps' not in link:
            raise forms.ValidationError('Invalid Google Maps link.')
        return link


from django import forms
from django.core.validators import RegexValidator
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()    
    phone = forms.CharField(
        max_length=15, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    message = forms.CharField(widget=forms.Textarea)
    
    
    
    

from django import forms
from .models import Perfilamiento

class PerfilamientoForm(forms.ModelForm):
    class Meta:
        model = Perfilamiento
        fields = '__all__'  # Include all fields
        labels = {
            'logo_agente': 'Logo Agente',
            'nombre_agente':'Nombre  del Agente',
            'cargo_en_la_agencia':'Cargo en la Agencia',
            'telefono_agente':'Telefono Agente',
            'email_agente':'Email Agente',
            'pagina_web':'Pagina Web',
            'ciudad_y_estado':'Ciudad Y Estado',
            'nombre_completo': 'Nombre Completo',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'estado_civil': 'Estado Civil',
            'domicilio': 'Domicilio',
            'colonia': 'Colonia',
            'ciudad': 'Ciudad',
            'codigo_postal': 'Código Postal',
            'telefono_contacto': 'Teléfono de Contacto',
            'rfc': 'RFC',
            'curp': 'CURP',
            'numero_identificacion_oficial': 'Número de Identificación Oficial',
            'ubicacion': 'Ubicación',
            'calle': 'Calle',
            'estado': 'Estado',
            'numero_exterior': 'Número Exterior',
            'tipo_inmueble': 'Tipo de Inmueble',
            'num_plantas': 'Número de Plantas',
            'cocina': 'Cocina',
            'num_recamaras': 'Número de Recámaras',
            'sala_estar': 'Sala de Estar',
            'num_banos': 'Número de Baños',
            'comedor': 'Comedor',
            'estacionamiento': 'Estacionamiento',
            'estudio': 'Estudio',
            'superficie_terreno': 'Superficie de Terreno',
            'superficie_construccion': 'Superficie de Construcción',
            'uso_suelo': 'Uso de Suelo',
            'antiguedad': 'Antigüedad',
            'forma_adquisicion': 'Forma de Adquisición',
            'grabamenes_propiedad': 'Grabámenes de Propiedad',
            'jardin': 'Jardín',
            'paneles_solares': 'Paneles Solares',
            'aire_acondicionado': 'Aire Acondicionado',
            'alberca': 'Alberca',
        }
    
    def __init__(self, *args, **kwargs):
        super(PerfilamientoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.attrs.update({'type': 'date'})
        self.fields['telefono_contacto'].widget.attrs.update({'placeholder': 'Ej. 55-1234-5678'})
        # Puedes agregar más personalizaciones aquí


from .models import FichaTecnica

class FichaTecnicaForm(forms.ModelForm):
    class Meta:
        model = FichaTecnica
        fields = '__all__'  # Include all fields
        labels = {
            "INFORMACIÓN AGENTE"
            'logo_agente': 'Logo Agente',
            'nombre_agente':'Nombre  del Agente',
            'cargo_en_la_agencia':'Cargo en la Agencia',
            'telefono_agente':'Telefono Agente',
            'email_agente':'Email Agente',
            'pagina_web':'Pagina Web',
            'ciudad_y_estado':'Ciudad Y Estado',
            
            'estado_conservacion': 'Estado de Conservación',
            'superficie_terreno': 'Superficie de Terreno (m²)',
            'superficie_construccion': 'Superficie de Construcción (m²)',
            'instalaciones_especiales': 'Instalaciones Especiales',
            'distribucion_materiales': 'Distribución y Materiales de Construcción',
            'infraestructura_zona': 'Infraestructura de la Zona y Urbanización',
            'antiguedad': 'Antigüedad (años)',
            'precio_venta': 'Precio de Venta',
            'urbanizacion': 'Urbanización',
            'situacion_legal': 'Situación Legal',
            'foto_1': 'Foto 1',
            'foto_2': 'Foto 2',
            'foto_3': 'Foto 3',
            'foto_4': 'Foto 4',
        }


from .models import InfoExtra

# Define the choices for condition fields
CONDITION_CHOICES = [
    ('Buen Estado', 'Buen Estado'),
    ('Regular', 'Regular'),
    ('Mal Estado', 'Mal Estado'),
]

from django import forms
from .models import InfoExtra

class InfoExtraForm(forms.ModelForm):
    # Other ChoiceFields
    fachada = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de la fachada', required=False)
    pintura = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de la pintura', required=False)
    humedades = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de humedades', required=False)
    grietas = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de grietas', required=False)
    undimientos = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de hundimientos', required=False)
    plomeria = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de plomería', required=False)
    vidrieria = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de vidriería', required=False)
    instalaciones_electricas = forms.ChoiceField(choices=CONDITION_CHOICES, label='Estado de instalaciones eléctricas', required=False)

    # Adding logo_agente as an ImageField for file upload
    logo_agente = forms.ImageField(label='Logo Agente', required=False)  # Define logo_agente as an ImageField

    class Meta:
        model = InfoExtra
        fields = '__all__'  # Include all fields, including logo_agente
        labels = {   
            'logo_agente': 'Logo Agente',
            'nombre_agente': 'Nombre del Agente',
            'cargo_en_la_agencia': 'Cargo en la Agencia',
            'telefono_agente': 'Telefono Agente',
            'email_agente': 'Email Agente',
            'pagina_web': 'Pagina Web Agente',
            'ciudad_y_estado': 'Ciudad Y Estado',

            'nombre_del_propietario': 'Nombre del propietario',
            'ciudad': 'Ciudad',
            'colonia': 'Colonia',
            'calle': 'Calle',
            'exterior': 'Número exterior',
            'estado': 'Estado',
            'cp': 'Código Postal',
            'estado_de_conservacion': 'Estado de conservación',
            'fachada': 'Estado de la fachada',
            'pintura': 'Estado de la pintura',
            'humedades': 'Estado de humedades',
            'grietas': 'Estado de grietas',
            'undimientos': 'Estado de hundimientos',
            'plomeria': 'Estado de plomería',
            'vidrieria': 'Estado de vidriería',
            'instalaciones_electricas': 'Estado de instalaciones eléctricas',
            'superficie_de_terreno': 'Superficie de terreno',
            'superficie_de_construccion': 'Superficie de construcción',
            'instalaciones_especiales': 'Instalaciones especiales',
            'distribucion': 'Distribución',
            'materiales_de_construccion': 'Materiales de construcción',
            'acabados': 'Acabados',
            'equipamiento_general': 'Equipamiento general',
            'infraestructura_y_urbanizacion': 'Infraestructura y urbanización',
            'antiguedad_de_la_construccion': 'Antigüedad de la construcción',
        }
