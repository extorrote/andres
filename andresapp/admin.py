from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import Agente, Venta, Alquiler, Terreno, PreConstruccion, Perfilamiento, FichaTecnica, InfoExtra

# Personalización de los títulos del panel de administración
admin.site.site_header = 'Panel de Administración casapv.com'
admin.site.site_title = 'Administración de casapv.com'
admin.site.index_title = 'Administra tús Propiedades Aqui'

# Personalización de los modelos en el Admin
@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo', 'años_de_experiencia')
    search_fields = ('nombre', 'correo')
    list_filter = ('años_de_experiencia',)
    list_per_page = 20  # Muestra más registros por página

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('colonia', 'precio', 'tipo_de_propiedad', 'agente')
    search_fields = ('colonia', 'tipo_de_propiedad')
    list_filter = ('condiciones_de_la_propiedad', 'agente', 'precio')
    list_per_page = 20

@admin.register(Alquiler)
class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('colonia', 'precio', 'tipo_de_propiedad', 'agente')
    search_fields = ('colonia', 'tipo_de_propiedad')
    list_filter = ('condiciones_de_la_propiedad', 'agente')
    list_per_page = 20

class TerrenoAdmin(admin.ModelAdmin):
    list_display = ('ubicacion', 'precio', 'medidas', 'agente', 'created', 'updated')
    search_fields = ('ubicacion', 'agente__nombre')  
    list_filter = ('agente', 'created', 'updated')
    list_per_page = 20

admin.site.register(Terreno, TerrenoAdmin)

@admin.register(PreConstruccion)
class PreConstruccionAdmin(admin.ModelAdmin):
    list_display = ('ubicacion', 'precio_normal', 'tipo_de_proyecto', 'agente')
    search_fields = ('ubicacion', 'tipo_de_proyecto')
    list_filter = ('agente',)
    list_per_page = 20

@admin.register(Perfilamiento)
class PerfilamientoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'fecha_nacimiento', 'estado_civil', 'ciudad', 'telefono_contacto')
    search_fields = ('nombre_completo', 'estado_civil', 'ciudad')
    list_filter = ('estado_civil', 'ciudad')
    list_per_page = 20

@admin.register(FichaTecnica)
class FichaTecnicaAdmin(admin.ModelAdmin):
    list_display = ('estado_conservacion', 'superficie_terreno', 'superficie_construccion', 'precio_venta')
    search_fields = ('estado_conservacion', 'precio_venta')
    list_filter = ('estado_conservacion',)
    list_per_page = 20

@admin.register(InfoExtra)
class InfoExtraAdmin(admin.ModelAdmin):
    list_display = ('nombre_del_propietario', 'ciudad', 'estado_de_conservacion')
    search_fields = ('nombre_del_propietario', 'ciudad')
    list_filter = ('estado_de_conservacion',)
    list_per_page = 20

# Personalización del AdminSite para agregar estilos CSS personalizados
class CustomAdminSite(admin.AdminSite):
    site_header = "Admin de casapv.com"
    site_title = "Administración de casapv.com"
    index_title = "Bienvenido al Panel de Administración de casapv.com"

    def each_context(self, request):
        context = super().each_context(request)
        # Inyectamos el archivo CSS personalizado para la interfaz de administración
        context['css_files'] = [static('css/admin.css')]  # Ruta a tu archivo CSS
        return context

# Usamos el AdminSite personalizado para registrar los modelos
admin_site = CustomAdminSite(name='custom_admin')

# Registrar los modelos con el AdminSite personalizado
admin_site.register(Agente, AgenteAdmin)
admin_site.register(Venta, VentaAdmin)
admin_site.register(Alquiler, AlquilerAdmin)
admin_site.register(Terreno, TerrenoAdmin)
admin_site.register(PreConstruccion, PreConstruccionAdmin)
admin_site.register(Perfilamiento, PerfilamientoAdmin)
admin_site.register(FichaTecnica, FichaTecnicaAdmin)
admin_site.register(InfoExtra, InfoExtraAdmin)

