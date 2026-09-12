from rest_framework import serializers
from .models import Categoria, Producto, Orden


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock', 'categoria']


class OrdenSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

    class Meta:
        model = Orden
        fields = ['id', 'fecha_creacion', 'estado', 'producto', 'cantidad']
        read_only_fields = ['fecha_creacion']
