from urllib import response
from rest_framework.viewsets import ModelViewSet
from frotas.api.serializers import FrotaSerializer, VeiculoSerializer, MotoristaSerializer, RastreamentoSerializer,ManutencaoSerializer, EventoTelemetriaSerializer, AlocacaoSerializer, AdvertenciaMotoristaSerializer
from frotas.models import Frota, Veiculo, Motorista, Rastreamento, Manutencao, Alocacao, EventoTelemetria, AdvertenciaMotorista
from rest_framework.decorators import action

class FrotaViewSet(ModelViewSet):
    queryset = Frota.objects.all()
    serializer_class = FrotaSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class MotoristaViewSet(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class RastreamentoViewSet(ModelViewSet):
    queryset = Rastreamento.objects.all()
    serializer_class = RastreamentoSerializer

    @action(detail=False, methods=['post'])
    def processar_localizacao(self, request):
        veiculo_id = request.data.get("veiculo_id")
        localizacao = request.data.get("localizacao")
        velocidade = request.data.get("velocidade")
        
        try:
            veiculo = Veiculo.objects.get(id=veiculo_id)
        except Veiculo.DoesNotExist:
            return response({"erro": "Veículo não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        if velocidade > 80:
            EventoTelemetria.objects.create(veiculo=veiculo, tipo_evento="Velocidade excessiva")
            
            alocacao = Alocacao.objects.filter(veiculo=veiculo, data_fim__isnull=True).first()
            if alocacao and AdvertenciaMotorista.objects.filter(motorista=alocacao.motorista).count() >= 3:
                AdvertenciaMotorista.objects.create(motorista=alocacao.motorista, mensagem="Dirigindo em alta velocidade repetidamente")
        
        Rastreamento.objects.create(veiculo=veiculo, localizacao=localizacao, velocidade=velocidade)
        
        if velocidade == 0:
            alertas = Rastreamento.objects.filter(veiculo=veiculo, velocidade=0).count()
            if alertas > 5:
                return response({"alerta": "Veículo parado por muito tempo!"})
        
        return response({"mensagem": "Localização e velocidade processadas com sucesso"})


class ManutencaoViewSet(ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer

class AlocacaoViewSet(ModelViewSet):
    queryset = Alocacao.objects.all()
    serializer_class = AlocacaoSerializer

class EventoTelemetriaViewSet(ModelViewSet):
    queryset = EventoTelemetria.objects.all()
    serializer_class = EventoTelemetriaSerializer

class AdvertenciaMotoristaViewSet(ModelViewSet):
    queryset = AdvertenciaMotorista.objects.all()
    serializer_class = AdvertenciaMotoristaSerializer