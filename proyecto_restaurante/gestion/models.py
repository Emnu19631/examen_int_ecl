from django.db import models

class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - S/{self.precio}"

class Comensal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Comensal, on_delete=models.CASCADE)


    def __str__(self):
        return f"Pedido de {self.cliente} - {self.fecha}"