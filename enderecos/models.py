from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=168)
    linha2 = models.CharField(max_length=168, null=True, blank=True)
    cidade = models.CharField(max_length=168)
    estado = models.CharField(max_length=64)
    pais = models.CharField(max_length=64)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1