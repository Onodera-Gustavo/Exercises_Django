from django.contrib import admin
from .models import Medico, Especialidade

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativa')
    list_filter = ('ativa',)
    search_fields = ('nome',)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'crm', 'especialidade', 'ativo', 'criado_em')
    list_filter = ('ativo', 'especialidade')
    search_fields = ('nome', 'crm', 'email')
    autocomplete_fields = ('especialidade',)
