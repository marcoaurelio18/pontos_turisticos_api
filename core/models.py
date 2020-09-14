from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class DocIdentificacao(models.Model):
    descricao = models.CharField(max_length=128)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=168)
    descricao = models.TextField()
    status = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    doc_identificacao = models.OneToOneField(DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
