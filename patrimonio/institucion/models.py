from django.db import models


class Museo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False)
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField()

    def __str__(self):
        return (
            f"Museo: {self.nombre} - Ciudad: {self.ciudad} - "
            f"Año de fundación: {self.anio_fundacion} - "
            f"Costo total de producción: {self.obtener_costo_total_produccion()} - "
            f"Guía(s) con más experiencia: {self.obtener_guias_mas_experiencia()}"
        )

    def obtener_costo_total_produccion(self):
        total = 0

        guias = GuiaMuseo.objects.filter(museo=self)

        for guia in guias:
            exhibiciones = Exhibicion.objects.filter(guia_museo=guia)

            for exhibicion in exhibiciones:
                total = total + exhibicion.costo_produccion

        return total

    def obtener_guias_mas_experiencia(self):
        guias = GuiaMuseo.objects.filter(museo=self)

        mayor_experiencia = 0

        for guia in guias:
            if guia.anios_experiencia_guia > mayor_experiencia:
                mayor_experiencia = guia.anios_experiencia_guia

        nombres_guias = ""

        for guia in guias:
            if guia.anios_experiencia_guia == mayor_experiencia:
                nombres_guias = nombres_guias + guia.nombre_completo + ", "

        if nombres_guias:
            return nombres_guias[:-2]

        return "Sin guías registrados"


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=150)
    anios_experiencia_guia = models.IntegerField()
    idiomas_hablados = models.CharField(max_length=200)
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Guía: {self.nombre_completo} - "
            f"Años de experiencia: {self.anios_experiencia_guia} - "
            f"Idiomas: {self.idiomas_hablados} - "
            f"Museo: {self.museo.nombre}"
        )


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=150)
    duracion_meses = models.IntegerField()
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    tematica = models.CharField(max_length=100)
    guia_museo = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Exhibición: {self.titulo_exhibicion} - "
            f"Duración: {self.duracion_meses} meses - "
            f"Costo: {self.costo_produccion} - "
            f"Temática: {self.tematica} - "
            f"Guía: {self.guia_museo.nombre_completo}"
        )