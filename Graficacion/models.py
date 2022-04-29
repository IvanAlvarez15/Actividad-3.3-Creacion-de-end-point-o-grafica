from django.db import models


class Canciones(models.Model):
    Nombre= models.CharField(max_length=50)
    Duracion = models.CharField(max_length=30)
    Genero= models.CharField(max_length=30)
    Ritmo= models.CharField(max_length=30)
    Dificultad = models.CharField(max_length=30)

class Historial(models.Model):
    Nombre_usuario= models.CharField(max_length=50)
    #Nombre_usuario= models.CharField(Usuarios, on_delete=models.CASCADE)
    ID_Usuario= models.CharField(max_length=30)
    Puntos_por_partida= models.CharField(max_length=30)
    Fecha_del_juego= models.CharField(max_length=30)
    ID_Canciones= models.CharField(max_length=30)
    Tiempo_jugado = models.CharField(max_length=30)
    