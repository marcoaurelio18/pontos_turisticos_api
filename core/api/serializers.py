from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracao = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'status', 'foto',
                  'atracao', 'endereco', 'comentarios', 'avaliacoes',
                  'descricao_completa',
                  )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
