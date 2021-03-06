from django.db import models

class Risco(models.IntegerChoices):
    BAIXO = 0, 'Baixo'
    MEDIO = 1, 'Médio'
    ALTO = 2, 'Alto'

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    data_de_inicio = models.DateField('Data de início')
    data_de_termino = models.DateField('Data de término')
    valor = models.IntegerField('Valor')
    risco = models.IntegerField(default=Risco.BAIXO, choices=Risco.choices)

    def __str__(self):
        return '%s' % (self.nome)

    @property
    def numero_de_participantes(self):
        # Retorna o numero de participantes vinculados ao projeto
        return Participante.objects.filter(projeto_vinculado=self).count()

class Participante(models.Model):
    nome = models.CharField(max_length=200)
    # O participante pode nao estar vinculado a um projeto
    projeto_vinculado = models.ForeignKey(Projeto, on_delete=models.PROTECT, blank=True, null=True)
