# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class AdminPersona(admin.ModelAdmin):
    list_display = ["cedula", "nombre", "telefono"]
    list_filter = ["fecha"]
    list_editable = ["telefono"]
    search_fields = ["cedula", "nombre"]
    class Meta:
        model = Persona

admin.site.register(Persona)
admin.site.register(Celulas)
admin.site.register(Servicio)
admin.site.register(Registrado)
admin.site.register(Galeria)


# Register your models here.
