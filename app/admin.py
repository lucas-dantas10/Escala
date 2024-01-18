from django.contrib import admin
from app import models


@admin.register(models.Participacao)
class ParticipacaoAdmin(admin.ModelAdmin):
    ...
@admin.register(models.Missa)
class MissaAdmin(admin.ModelAdmin):
    ...
@admin.register(models.Escala)
class EscalaAdmin(admin.ModelAdmin):
    ...