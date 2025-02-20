from rest_framework.serializers import ModelSerializer
from frotas.models import Frota, Veiculo, Motorista, Rastreamento, Manutencao, Alocacao, EventoTelemetria, AdvertenciaMotorista

class FrotaSerializer(ModelSerializer):
    class Meta:
        model = Frota
        fields = '__all__'

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'

class RastreamentoSerializer(ModelSerializer):
    class Meta:
        model = Rastreamento
        fields = '__all__'

class ManutencaoSerializer(ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'

class AlocacaoSerializer(ModelSerializer):
    class Meta:
        model = Alocacao
        fields = '__all__'

class EventoTelemetriaSerializer(ModelSerializer):
    class Meta:
        model = EventoTelemetria
        fields = '__all__'

class AdvertenciaMotoristaSerializer(ModelSerializer):
    class Meta:
        model = AdvertenciaMotorista
        fields = '__all__'