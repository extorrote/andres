from django.db import models

from django.db import models

class Agente(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    correo = models.EmailField(max_length=50, null=True, blank=True)
    foto = models.ImageField(upload_to='andresapp/agentes', null=True, blank=True)
    años_de_experiencia = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre or 'Unnamed Agent'


class Venta(models.Model):
    # Your existing fields...
    colonia = models.CharField(max_length=150, null=True, blank=True)
    precio = models.CharField(max_length=50, null=True, blank=True)
    habitaciones = models.CharField(max_length=50, null=True, blank=True)
    baños = models.CharField(max_length=50, null=True, blank=True)
    #NUEVOS
    cocina=models.CharField(max_length=50, null=True, blank=True)
    jardin=models.CharField(max_length=50, null=True, blank=True)
    comedor=models.CharField(max_length=50, null=True, blank=True)
    balcon=models.CharField(max_length=50, null=True, blank=True)
    ###
    cuarto_de_servicio = models.CharField(max_length=50, null=True, blank=True) 
    piscina = models.CharField(max_length=50, null=True, blank=True)
    amoblado = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_propiedad = models.CharField(max_length=200, null=True, blank=True)
    medidas_de_la_propiedad = models.CharField(max_length=40, null=True, blank=True)
    sala = models.CharField(max_length=50, null=True, blank=True)
    #agregar superficie de construccion
    numero_de_piso = models.CharField(max_length=150, null=True, blank=True)
    amoblado = models.CharField(max_length=150, null=True, blank=True)
    privada_o_con_escrituras = models.CharField(max_length=150, null=True, blank=True)
    electrodomesticos_y_muebles_en_general = models.CharField(max_length=250, null=True, blank=True)
    paredes = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_calle = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_electricidad = models.CharField(max_length=150, null=True, blank=True)
    informacion_extra = models.CharField(max_length=700, null=True, blank=True)
    comodidades_en_areas_comunes = models.CharField(max_length=150, null=True, blank=True)
    elevador = models.CharField(max_length=150, null=True, blank=True)
    rooftop = models.CharField(max_length=150, null=True, blank=True)
    gym = models.CharField(max_length=150, null=True, blank=True)
    estasionamiento = models.CharField(max_length=150, null=True, blank=True)
    condiciones_de_la_propiedad = models.CharField(max_length=50, null=True, blank=True)
    pet_friendly = models.CharField(max_length=50, null=True, blank=True)
    vista_primaria = models.CharField(max_length=50, null=True, blank=True)
    vista_secundaria = models.CharField(max_length=50, null=True, blank=True)
    imagen1 = models.ImageField(upload_to='andresapp', null=True, blank=True) #AGREGAMOS 8 FOTOS MAS
    imagen2 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen6 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen7 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen8 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen9 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen10 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen11 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen12 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen13 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen14 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen15 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen16 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    youtube_link = models.TextField(blank=True, default="", null=True)
    agua = models.CharField(max_length=500, null=True, blank=True)
    tipo_tipo_de_estufa = models.CharField(max_length=150, null=True, blank=True)
    aire_acondicionado = models.CharField(max_length=150, null=True, blank=True)
    calentador_de_agua = models.CharField(max_length=150, null=True, blank=True)
    pago_de_mantenimiento = models.CharField(max_length=250, null=True, blank=True)
    que_incluye_el_pago_de_mantenimiento = models.CharField(max_length=250, null=True, blank=True)
    direccion_exacta = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link_de_google_maps = models.CharField(max_length=500, null=True, blank=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='ventas')

    def get_object_url(self):
        return f'/ventas/{self.id}/'  # Changed to match your URLs

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return self.colonia or 'Unnamed Sale'


# The rest of your models (Alquiler, Terreno, PreConstruccion) remain unchanged.



class Alquiler(models.Model):
    # Fields as in Venta model, but tailored for rental properties
    colonia = models.CharField(max_length=150, null=True, blank=True)
    precio = models.CharField(max_length=50, null=True, blank=True)
    habitaciones = models.CharField(max_length=50, null=True, blank=True)
    baños = models.CharField(max_length=50, null=True, blank=True)
    sala = models.CharField(max_length=50, null=True, blank=True)
    #NUEVOS
    cocina=models.CharField(max_length=50, null=True, blank=True)
    jardin=models.CharField(max_length=50, null=True, blank=True)
    comedor=models.CharField(max_length=50, null=True, blank=True)
    balcon=models.CharField(max_length=50, null=True, blank=True)
    ###
    cuarto_de_servicio = models.CharField(max_length=50, null=True, blank=True) #NUEVO
    tipo_de_propiedad = models.CharField(max_length=200, null=True, blank=True)
    numero_de_piso = models.CharField(max_length=150, null=True, blank=True)
    elevador = models.CharField(max_length=150, null=True, blank=True)
    amoblado = models.CharField(max_length=150, null=True, blank=True)
    vista_primaria = models.CharField(max_length=50, null=True, blank=True)
    vista_secundaria = models.CharField(max_length=50, null=True, blank=True)   
    rooftop = models.CharField(max_length=150, null=True, blank=True)
    gym = models.CharField(max_length=150, null=True, blank=True)
    estasionamiento = models.CharField(max_length=150, null=True, blank=True)
    electrodomesticos_y_muebles_en_general = models.CharField(max_length=250, null=True, blank=True)
    condiciones_de_la_propiedad = models.CharField(max_length=50, null=True, blank=True)
    tipo_de_electricidad = models.CharField(max_length=150, null=True, blank=True)
    medidas_de_la_propiedad = models.CharField(max_length=40, null=True, blank=True)
    requisitos = models.TextField(blank=True, null=True)
    duracion_contrato = models.CharField(max_length=50, null=True, blank=True)
    deposito = models.CharField(max_length=50, null=True, blank=True)
    areas_comunes = models.CharField(max_length=250, null=True, blank=True)
    piscina = models.CharField(max_length=50, null=True, blank=True)
    pet_friendly = models.CharField(max_length=50, null=True, blank=True)
    tipo_tipo_de_estufa = models.CharField(max_length=150, null=True, blank=True)
    aire_acondicionado = models.CharField(max_length=150, null=True, blank=True)
    calentador_de_agua = models.CharField(max_length=150, null=True, blank=True)
    pago_de_mantenimiento = models.CharField(max_length=250, null=True, blank=True)
    que_incluye_el_pago_de_mantenimiento = models.CharField(max_length=250, null=True, blank=True)
    informacion_extra = models.CharField(max_length=700, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    imagen1 = models.ImageField(upload_to='andresapp', null=True, blank=True) #AGREGAMOS 8 FOTOS MAS
    imagen2 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen6 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen7 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen8 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen9 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen10 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen11 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen12 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen13 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen14 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen15 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen16 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    youtube_link = models.TextField(blank=True, default="", null=True)
    direccion_exacta = models.CharField(max_length=50, null=True, blank=True)
    link_de_google_maps = models.CharField(max_length=500, null=True, blank=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='alquileres')

    class Meta:
        verbose_name = 'Renta'
        verbose_name_plural = 'Rentas'


class Terreno(models.Model):
    ubicacion = models.CharField(max_length=50, null=True, blank=True)
    precio = models.CharField(max_length=50, null=True, blank=True)
    medidas = models.CharField(max_length=50, null=True, blank=True)
    metros_cuadrados=models.CharField(max_length=50, null=True, blank=True)
    propiedad_privada_o_con_escrituras = models.CharField(max_length=50, null=True, blank=True)
    uso_de_suelo = models.CharField(max_length=50, null=True, blank=True)
    informacion_extra = models.CharField(max_length=700, null=True, blank=True)
    imagen1 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen2 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen6 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen7 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen8 = models.ImageField(upload_to='andresapp', null=True, blank=True)# DEJAR EN 8 FOTOS
    youtube_link = models.TextField(blank=True, default="", null=True)
    direccion_exacta = models.CharField(max_length=50, null=True, blank=True)
    link_de_google_maps = models.CharField(max_length=500, null=True, blank=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='terrenos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Terreno'
        verbose_name_plural = 'Terrenos'


class PreConstruccion(models.Model): 
    ubicacion = models.CharField(max_length=150, null=True, blank=True)
    precio_normal = models.CharField(max_length=50, null=True, blank=True)
    precio_preventa = models.CharField(max_length=50, null=True, blank=True)
    anticipo = models.CharField(max_length=50, null=True, blank=True)  # ANTICIPO O ENGANCHE
    tipo_de_proyecto = models.CharField(max_length=200, null=True, blank=True)
    habitaciones = models.CharField(max_length=50, null=True, blank=True, default=" ")
    baños = models.CharField(max_length=50, null=True, blank=True)
    sala = models.CharField(max_length=50, null=True, blank=True)
    cuarto_de_servicio = models.CharField(max_length=50, null=True, blank=True) 
    fecha_entrega = models.CharField(max_length=50, null=True, blank=True) 
    cocina = models.CharField(max_length=50, null=True, blank=True)
    #NUEVOS
    politicas_de_venta=models.CharField(max_length=50, null=True, blank=True)
    jardin=models.CharField(max_length=50, null=True, blank=True)
    comedor=models.CharField(max_length=50, null=True, blank=True)
    balcon=models.CharField(max_length=50, null=True, blank=True)
    escrituras=models.CharField(max_length=50, null=True, blank=True)
    medidas = models.CharField(max_length=50, null=True, blank=True)
    metros_cuadrados=models.CharField(max_length=50, null=True, blank=True)
    ###
    se_entrega_con = models.CharField(max_length=250, null=True, blank=True)
    areas_comunes = models.CharField(max_length=250, null=True, blank=True)
    piscina = models.CharField(max_length=250, null=True, blank=True)
    numero_de_piso = models.CharField(max_length=150, null=True, blank=True)
    numero_de_departamento=models.CharField(max_length=150, null=True, blank=True)
    elevador = models.CharField(max_length=150, null=True, blank=True)
    rooftop = models.CharField(max_length=150, null=True, blank=True)
    gym = models.CharField(max_length=150, null=True, blank=True)
    estasionamiento = models.CharField(max_length=150, null=True, blank=True)
    electrodomesticos_y_muebles_en_general = models.CharField(max_length=250, null=True, blank=True)
    agua = models.CharField(max_length=500, null=True, blank=True)   
    amoblado = models.CharField(max_length=150, null=True, blank=True)   
    paredes = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_calle = models.CharField(max_length=150, null=True, blank=True)
    tipo_de_electricidad = models.CharField(max_length=150, null=True, blank=True)
    comodidades_en_areas_comunes = models.CharField(max_length=150, null=True, blank=True) #CAMBIAR A AMENIDADES
    aire_acondicionado = models.CharField(max_length=150, null=True, blank=True)
    calentador_de_agua = models.CharField(max_length=150, null=True, blank=True)
    informacion_extra = models.TextField(blank=True, null=True)
    imagen1 = models.ImageField(upload_to='andresapp', null=True, blank=True) #AGREGAMOS 8 FOTOS MAS
    imagen2 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen3 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen4 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen5 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen6 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen7 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen8 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen9 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen10 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen11 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen12 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen13 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen14 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen15 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    imagen16 = models.ImageField(upload_to='andresapp', null=True, blank=True)
    youtube_link = models.TextField(blank=True, default="", null=True)
    direccion_exacta = models.CharField(max_length=50, null=True, blank=True)
    link_de_google_maps = models.CharField(max_length=500, null=True, blank=True)
    agente = models.ForeignKey(Agente, on_delete=models.CASCADE, related_name='pre_construcciones')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pre-Venta'
        verbose_name_plural = 'Pre-ventas'
        
        
        



from django.db import models

class Perfilamiento(models.Model):
    
    #INFORMACION DEL AGENTE : 
    logo_agente=models.ImageField(upload_to='andresapp/agentes', null=True, blank=True)
    nombre_agente=models.CharField(max_length=255, blank=True, null=True)
    cargo_en_la_agencia=models.CharField(max_length=255, blank=True, null=True)
    telefono_agente=models.CharField(max_length=255, blank=True, null=True)
    email_agente=models.CharField(max_length=255, blank=True, null=True)
    pagina_web=models.CharField(max_length=255, blank=True, null=True)
    ciudad_y_estado=models.CharField(max_length=255, blank=True, null=True)






    nombre_completo = models.CharField(max_length=255)
    fecha_nacimiento = models.CharField(max_length=10)  # Considera usar DateField si es apropiado
    estado_civil = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=255)
    colonia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono_contacto = models.CharField(max_length=15)
    rfc = models.CharField(max_length=20)
    curp = models.CharField(max_length=20)
    numero_identificacion_oficial = models.CharField(max_length=50)   
    ubicacion = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    tipo_inmueble = models.CharField(max_length=50)    
    num_plantas = models.CharField(max_length=10)
    cocina = models.CharField(max_length=50)
    num_recamaras = models.CharField(max_length=10)
    sala_estar = models.CharField(max_length=50)
    num_banos = models.CharField(max_length=10)
    comedor = models.CharField(max_length=50)
    estacionamiento = models.CharField(max_length=10)
    estudio = models.CharField(max_length=50)
    superficie_terreno = models.CharField(max_length=10)
    superficie_construccion = models.CharField(max_length=10)
    uso_suelo = models.CharField(max_length=50)
    antiguedad = models.CharField(max_length=10)
    forma_adquisicion = models.CharField(max_length=50)
    grabamenes_propiedad = models.CharField(max_length=255)
    jardin = models.CharField(max_length=50)
    paneles_solares = models.CharField(max_length=50)
    aire_acondicionado = models.CharField(max_length=50)
    alberca = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_completo



class FichaTecnica(models.Model):
    
    logo_agente=models.ImageField(upload_to='andresapp/agentes', null=True, blank=True)
    nombre_agente=models.CharField(max_length=255, blank=True, null=True)
    cargo_en_la_agencia=models.CharField(max_length=255, blank=True, null=True)
    telefono_agente=models.CharField(max_length=255, blank=True, null=True)
    email_agente=models.CharField(max_length=255, blank=True, null=True)
    pagina_web=models.CharField(max_length=255, blank=True, null=True)
    ciudad_y_estado=models.CharField(max_length=255, blank=True, null=True)
    
    estado_conservacion = models.CharField(max_length=250)
    superficie_terreno = models.CharField(max_length=250)
    superficie_construccion = models.CharField(max_length=250)
    instalaciones_especiales = models.CharField(max_length=250,blank=True)
    distribucion_materiales = models.CharField(max_length=250,blank=True)
    infraestructura_zona = models.CharField(max_length=250,blank=True)
    antiguedad = models.CharField(max_length=250)
    precio_venta = models.CharField(max_length=250, blank=True, null=True)
    urbanizacion = models.CharField(max_length=250 ,blank=True, null=True)
    situacion_legal = models.CharField(max_length=250,blank=True)
    
    # Campos para fotografías del bien inmueble
    foto_1 = models.ImageField(upload_to='ficha_tectica/fotos/', blank=True, null=True)
    foto_2 = models.ImageField(upload_to='ficha_tectica/fotos/', blank=True, null=True)
    foto_3 = models.ImageField(upload_to='ficha_tectica/fotos/', blank=True, null=True)
    foto_4 = models.ImageField(upload_to='ficha_tectica/fotos/', blank=True, null=True)

    def __str__(self):
        return f"Ficha Técnica: {self.estado_conservacion}, Precio: {self.precio_venta} "





class InfoExtra(models.Model):
    logo_agente=models.ImageField(upload_to='andresapp/agentes', null=True, blank=True)
    nombre_agente=models.CharField(max_length=255, blank=True, null=True)
    cargo_en_la_agencia=models.CharField(max_length=255, blank=True, null=True)
    telefono_agente=models.CharField(max_length=255, blank=True, null=True)
    email_agente=models.CharField(max_length=255, blank=True, null=True)
    pagina_web=models.CharField(max_length=255, blank=True, null=True)
    ciudad_y_estado=models.CharField(max_length=255, blank=True, null=True)
    
    
    nombre_del_propietario = models.CharField(max_length=500,blank=True, null=True)   
    ciudad= models.CharField(max_length=500,blank=True, null=True)
    colonia= models.CharField(max_length=500,blank=True, null=True)
    calle= models.CharField(max_length=500,blank=True, null=True)
    exterior= models.CharField(max_length=500,blank=True, null=True)
    estado= models.CharField(max_length=500,blank=True, null=True)
    cp= models.CharField(max_length=500,blank=True, null=True)
    estado_de_conservacion = models.CharField(max_length=500,blank=True, null=True)
    fachada=models.CharField(max_length=500,blank=True, null=True)
    pintura=models.CharField(max_length=500,blank=True, null=True)
    humedades=models.CharField(max_length=500,blank=True, null=True)
    grietas=models.CharField(max_length=500,blank=True, null=True)
    undimientos=models.CharField(max_length=500,blank=True, null=True)
    plomeria=models.CharField(max_length=500,blank=True, null=True)
    vidrieria=models.CharField(max_length=500,blank=True, null=True)
    instalaciones_electricas=models.CharField(max_length=500,blank=True, null=True)
    superficie_de_terreno = models.CharField(max_length=500)
    superficie_de_construccion = models.CharField(max_length=500,blank=True, null=True)
    instalaciones_especiales = models.CharField(max_length=500)
    distribucion = models.CharField(max_length=500,blank=True, null=True)
    materiales_de_construccion = models.CharField(max_length=500,blank=True, null=True)
    acabados = models.CharField(max_length=500,blank=True, null=True)
    equipamiento_general = models.CharField(max_length=500,blank=True, null=True)
    infraestructura_y_urbanizacion = models.CharField(max_length=500,blank=True, null=True)
    antiguedad_de_la_construccion = models.CharField(max_length=500,blank=True, null=True)
    class Meta:
        verbose_name = 'Levantamiento'
        verbose_name_plural = 'Levantamientos'
        
        
    def __str__(self):
        return self.nombre_del_propietario  # You can change this as needed
        