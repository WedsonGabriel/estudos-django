from django.db import models

class Despesa(models.Model):
    descricao = models.CharField(verbose_name="descrição", max_length=200, blank=False, null=False)
    categoria = models.CharField(verbose_name="categoria", max_length=50, blank=False, null=False)
    valor = models.DecimalField(verbose_name="valor", max_digits=20, decimal_places=2, blank=False, null=False)
    data = models.DateField(verbose_name="data", blank=False, null=False)
    pago = models.BooleanField(verbose_name="pago", default=True)

    def __str__(self):
        return f"Descrição: {Despesa.descricao}, Categoria: {Despesa.categoria}, Valor: {Despesa.valor}, Data: {Despesa.data}"
