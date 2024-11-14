"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from andresapp import views 
from django.conf import settings
from django.conf.urls.static import static

from andresapp.views import Buscador_Ventas ,Buscador_Alquiler,Buscador_Terreno,Buscador_pre_ventas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('create-agent/', views.create_agent, name='create_agent'),
    path('create-venta/', views.create_venta, name='create_venta'),
    path('create-alquiler/', views.create_alquiler, name='create_alquiler'),
    path('create-terreno/', views.create_terreno, name='create_terreno'),
    path('create-pre-construccion/', views.create_pre_construccion, name='create_pre_construccion'),
    path('crear_perfilamiento/', views.crear_perfilamiento, name='crear_perfilamiento'),    
    path('crear_ficha_tecnica/', views.crear_ficha_tecnica, name='crear_ficha_tecnica'),
    

    path('editar_perfilamiento/<int:pk>/', views.editar_perfilamiento, name='editar_perfilamiento'),
    path('editar_ficha_tecnica/<int:pk>/', views.editar_ficha_tecnica, name='editar_ficha_tecnica'),
    
    path('crear_levantamiento/', views.create_info_extra, name='crear_levantamiento'),
    path('lista_levantamientos/', views.list_info_extra, name='lista_levantamientos'),
    path('editar_levantamiento/<int:pk>/', views.editar_levantamiento, name='editar_levantamientos'),  
     path('ultimo_documento/', views.ultimo_documento, name='ultimo_documento'), 
    
    path('', views.lista_ventas, name='home'),  # Changed to 'home' for clarity
    path('ventas/<int:pk>/', views.detalle_venta, name='detalle_venta'),  # Added detail view
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('alquileres/', views.alquiler_list, name='alquiler_list'),
    path('terrenos/', views.terrenos_list, name='terrenos_list'),
    path('pre_construcciones/', views.pre_construccion_list, name='pre_construccion_list'),
    path('perfilamiento_list/', views.perfilamiento_list, name='perfilamiento_list'),
    path('lista_fichas_tecnicas/', views.lista_fichas_tecnicas, name='lista_fichas_tecnicas'),

    path('alquiler/<int:pk>/', views.detalle_alquiler, name='detalle_alquiler'),  # Ensure this is defined
    path('terreno/<int:pk>/', views.terrenos_detail, name='terrenos_detail'),

    path('pre_construccion/<int:pk>/', views.pre_construccion_detail, name='pre_construccion_detail'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('enviar_email/', views.send_email, name="enviar_email"),
    path('about_us/', views.about_us, name="about_us"),
    
    path('api/search-properties/', views.Buscador_Ventas, name='search_properties'),
    path('buscador/', Buscador_Alquiler, name='buscador-alquiler'),
    path('api/buscador-terrenos/', Buscador_Terreno, name='buscador_terreno'),
    path('api/buscador_pre_ventas/', views.Buscador_pre_ventas, name='buscador_pre_ventas'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


