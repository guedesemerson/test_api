from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField()
    endereco = models.TextField()

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome