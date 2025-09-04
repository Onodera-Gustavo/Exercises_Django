from django.db import models

class Especialidade(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    descricao = models.TextField('Descrição', blank=True)
    ativa = models.BooleanField('Ativa', default=True)

    class Meta:
        db_table = 'especialidade'
        ordering = ['nome']
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField('Nome', max_length=150)
    crm = models.CharField('CRM', max_length=20, unique=True)
    email = models.EmailField('E-mail', unique=True, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, blank=True)
    data_nascimento = models.DateField('Data de nascimento', null=True, blank=True)
    ativo = models.BooleanField('Ativo', default=True)
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.PROTECT,
        related_name='medicos',
        verbose_name='Especialidade'
    )
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        db_table = 'medico'
        ordering = ['nome']
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return f'{self.nome} ({self.crm})'
