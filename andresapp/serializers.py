from rest_framework import serializers
from .models import Venta,Alquiler,Terreno,PreConstruccion

# serializers.py
from rest_framework import serializers
from .models import Venta

class VentaSerializer(serializers.ModelSerializer):
    # Adding a custom field to include the 'detail_url'
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Venta
        fields = ['id', 'colonia', 'habitaciones', 'baños', 'precio', 'detail_url']

    def get_detail_url(self, obj):
        # This will return the URL of the property detail page
        return obj.get_object_url()  # Assumes your model has a method to get the object URL

        


class AlquilerSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = Alquiler
        fields = ['id', 'colonia', 'habitaciones', 'baños', 'precio', 'detail_url']
        
    def get_detail_url(self, obj):
        # This will return the URL of the property detail page
        return obj.get_object_url()  # Assumes your model has a method to get the object URL
        


class TerrenoSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = Terreno
        fields = ['id', 'ubicacion', 'precio']
        
    def get_detail_url(self, obj):
        # This will return the URL of the property detail page
        return obj.get_object_url()  # Assumes your model has a method to get the object URL



class PreVentasSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = Terreno
        fields = ['id', 'ubicacion', 'precio_preventa', 'tipo_de_proyecto', 'habitaciones']
        
    def get_detail_url(self, obj):
        # This will return the URL of the property detail page
        return obj.get_object_url()  # Assumes your model has a method to get the object URL

