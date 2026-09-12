from django.db import models
from django.db import models

# Tabla Categoría: nombre, descripción
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Tabla Producto: nombre, precio, stock y relación a Categoria
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

# Tabla Orden: fecha_creacion, estado, relación a Producto y cantidad
class Orden(models.Model):
    ESTADO_CHOICES = [
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('rechazado', 'Rechazado'),
    ]

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='enviado')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ordenes')
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Orden #{self.id} - {self.estado}"