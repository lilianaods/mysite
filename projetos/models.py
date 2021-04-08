from django.db import models

class Risco(models.IntegerChoices):
    BAIXO = 0, 'Baixo'
    MEDIO = 1, 'Médio'
    ALTO = 2, 'Alto'

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    data_de_inicio = models.DateField('Data de início')
    data_de_termino = models.DateField('Data de término')
    valor = models.DecimalField('Valor' , max_digits=15, decimal_places=2)
    risco = models.IntegerField(default=Risco.BAIXO, choices=Risco.choices)

    def __str__(self):
        return '%s' % (self.nome)

class Participante(models.Model):
    nome = models.CharField(max_length=200)
    projeto_vinculado = models.ForeignKey(Projeto, on_delete=models.PROTECT)
