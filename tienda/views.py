from django.shortcuts import render

from rest_framework import viewsets
from .models import Categoria, Producto, Orden
from .serializers import CategoriaSerializer, ProductoSerializer, OrdenSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all().order_by('-fecha_creacion')
    serializer_class = OrdenSerializer
