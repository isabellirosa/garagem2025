from django.db import models
from django.forms import DecimalField, IntegerField

from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio


class Veiculo(models.Model):
    ano = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculo")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculo" )
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculo", blank=True)

    def __str__(self):
        return f"({self.id}) {self.modelo.marca} {self.modelo.nome} {self.cor.nome} {self.ano}"