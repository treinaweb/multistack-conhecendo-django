from django.db import models

# Create your models here.


class Tarefa(models.Model):
    STATUS_CHOICE = [
        (1, "A fazer"),
        (2, "Feito"),
        (3, "Finalizado")
    ]
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICE, null=False, blank=False)
