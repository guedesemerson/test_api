from django.db import models
from paciente.models import Paciente


class Exame(models.Model):
    nome_profissional = models.CharField(max_length=150)
    data_exame = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"

    def __str__(self):
        return self.nome_profissional