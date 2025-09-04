from django.urls import path
from . import views

urlpatterns = [
    path('especialidades/', views.especialidade_list, name='especialidade_list'),
    path('especialidades/novo/', views.especialidade_create, name='especialidade_create'),
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/novo/', views.medico_create, name='medico_create'),
]
