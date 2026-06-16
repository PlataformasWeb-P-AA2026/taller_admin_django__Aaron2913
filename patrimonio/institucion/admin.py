from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion


@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "ciudad",
        "anio_fundacion",
        "obtener_costo_total_produccion",
        "obtener_guias_mas_experiencia",
    )


@admin.register(GuiaMuseo)
class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_completo",
        "anios_experiencia_guia",
        "idiomas_hablados",
        "museo",
    )


@admin.register(Exhibicion)
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo_exhibicion",
        "duracion_meses",
        "costo_produccion",
        "tematica",
        "guia_museo",
    )