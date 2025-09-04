from django.shortcuts import render, redirect
from .models import Medico, Especialidade
from django.forms import ModelForm

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao', 'ativa']

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'email', 'telefone', 'data_nascimento', 'ativo', 'especialidade']

def especialidade_list(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'medico/especialidade_list.html', {'especialidades': especialidades})

def especialidade_create(request):
    form = EspecialidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('especialidade_list')
    return render(request, 'medico/especialidade_form.html', {'form': form})

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/medico_list.html', {'medicos': medicos})

def medico_create(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medico_list')
    return render(request, 'medico/medico_form.html', {'form': form})
