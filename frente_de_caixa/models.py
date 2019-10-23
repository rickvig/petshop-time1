from django.db import models
from datetime import datetime
from core.models import *


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_final = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    def itens_venda(self):
        pass

    def __str__(self):
        return self.cliente.__str__() + " - " + str(self.valor_final)


class ItensDeVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, blank=True, null=True)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.valor_total = self.quantidade * self.produto.valor_venda
        print('valor_total', self.valor_total)


        super().save(*args, **kwargs)

    def __str__(self):
        return self.produto.__str__() + " - " + str(self.quantidade)