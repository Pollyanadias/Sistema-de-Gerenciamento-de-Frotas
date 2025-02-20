from datetime import timezone
from django.db import models

# Create your models here.
from django.db import models

class Frota(models.Model):
    nome = models.CharField(max_length=255)
    
    def adicionar_veiculo(self, veiculo):
        veiculo.frota = self
        veiculo.save()
    
    def remover_veiculo(self, placa):
        veiculo = Veiculo.objects.filter(placa=placa, frota=self).first()
        if veiculo:
            veiculo.frota = None
            veiculo.save()
            return True
        return False
    
    def listar_veiculos(self):
        return self.veiculo_set.all()

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()
    status = models.CharField(max_length=50, choices=[('disponível', 'Disponível'), ('em uso', 'Em Uso'), ('manutenção', 'Manutenção')])
    frota = models.ForeignKey(Frota, on_delete=models.SET_NULL, null=True, blank=True)
    
    def rastrear(self):
        ultima_localizacao = Rastreamento.objects.filter(veiculo=self).order_by('-horario').first()
        return ultima_localizacao.localizacao if ultima_localizacao else "Localização desconhecida"
    
    def obter_detalhes(self):
        return f"{self.modelo} ({self.ano}) - Placa: {self.placa} - Status: {self.status}"

class Motorista(models.Model):
    nome = models.CharField(max_length=255)
    cnh = models.CharField(max_length=20, unique=True)
    
    def verificar_habilitacao(self):
        return bool(self.cnh)

class Rastreamento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    localizacao = models.CharField(max_length=255)
    horario = models.DateTimeField(auto_now_add=True)
    velocidade = models.FloatField()
    
    def atualizar_localizacao(self, nova_localizacao, nova_velocidade):
        self.localizacao = nova_localizacao
        self.velocidade = nova_velocidade
        self.save()
    
    def obter_ultima_localizacao(self):
        return self.localizacao

class Manutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()
    custo = models.FloatField()
    
    @staticmethod
    def obter_historico(veiculo):
        return Manutencao.objects.filter(veiculo=veiculo)

class Alocacao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    
    def registrar_alocacao(self, veiculo, motorista, data_inicio, data_fim):
        if Alocacao.verificar_disponibilidade(veiculo):
            self.veiculo = veiculo
            self.motorista = motorista
            self.data_inicio = data_inicio
            self.data_fim = data_fim
            self.save()
            return True
        return False
    
    @staticmethod
    def verificar_disponibilidade(veiculo):
        return not Alocacao.objects.filter(veiculo=veiculo, data_fim__isnull=True).exists()
    
    def encerrar_alocacao(self):
        self.data_fim = timezone.now()
        self.save()

class EventoTelemetria(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=255)
    data_hora = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def listar_eventos(veiculo):
        return EventoTelemetria.objects.filter(veiculo=veiculo)

class AdvertenciaMotorista(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    mensagem = models.TextField()
    
    @staticmethod
    def listar_advertencias(motorista):
        return AdvertenciaMotorista.objects.filter(motorista=motorista)
