### Projeto APS - Sistema de Controle de Frotas

### Levantamento de Requisitos

### Requisitos Funcionais:

Permitir o rastreamento em tempo real da localização dos veículos.
Exibir mapas com trajetos percorridos e informações detalhadas de cada veículo.
Registrar manutenções realizadas e notificar sobre manutenções preventivas.
Gerar relatórios de custos de manutenção.
Exibir lista de veículos disponíveis para alocação.
Alertar sobre inconsistências nos dados dos veículos.
Verificar a localização atual dos veículos.
Saber a velocidade dos veículos.
Conhecer o trajeto percorrido pelos veículos.
Verificar o tempo que os veículos permaneceram em um local específico.
Identificar eventos de telemetria importantes.
Corrigir ou advertir gestores responsáveis por irregularidades.
Listar os veículos cadastrados na frota.
Gerenciar a frota de veículos cadastrados.
Gerar alertas para manutenções pendentes ou atrasadas.

### Requisitos Não Funcionais:

O rastreamento deve ser atualizado a cada 5 segundos.
O sistema deve ser capaz de gerar relatórios mensais de custos de manutenção.
O sistema deve permitir consultas rápidas de alocações passadas e atuais.
A interface do sistema deve ser intuitiva e responsiva.
O sistema deve suportar até 500 usuários simultâneos.
O sistema deve garantir alta disponibilidade, com tolerância a falhas de até 99,9%.

### Regras de Negócio

### Autenticação de Usuários:

Somente usuários autenticados podem acessar as funcionalidades do sistema.
O gestor é o único autorizado a realizar operações administrativas, como exclusão de
dados.

### Rastreamento de Veículos:

O rastreamento deve ocorrer em tempo real com atualizações a cada 5 segundos.
O sistema deve emitir alerta caso algum veículo esteja fora da rota planejada.

### Manutenção Preventiva:

Manutenções preventivas devem ser registradas com base na quilometragem ou
tempo de uso.
Notificações automáticas devem ser enviadas ao gestor antes do vencimento.
O sistema deve impedir que veículos com manutenção atrasada sejam alocados.

### Relatórios:

Relatórios de custos e desempenho devem ser gerados mensalmente.
Todos os relatórios devem estar disponíveis para consulta em até 12 meses após sua
geração.

### Segurança dos Dados:
Os dados sensíveis devem ser protegidos com criptografia.
O sistema deve manter logs de todas as ações realizadas por usuários para auditoria.

### Capacidade de Escalabilidade:
O sistema deve ser capaz de gerenciar até 500 veículos simultaneamente.

### Relação de Casos de Uso

### Casos de Uso

### Listar Veículos

**Descrição:** Visualizar os veículos cadastrados dentro do sistema. 

**Atores:** Gestor da Frota.

### Rastrear Veículos
**Descrição:** Monitorar a localização em tempo real dos veículos da frota. 

**Atores:** Gestor da Frota.

### Gerenciar Manutenção
**Descrição:** Registrar manutenções realizadas e futuras, com notificações preventivas.
Permite a emissão de relatórios detalhados sobre os custos de manutenção da frota.

**Atores:** Gestor da Frota.

### Verificar a Localização do Veículo
**Descrição:** Permitir que o gestor visualize a localização atual de um veículo específico.

**Atores:** Gestor da Frota.

### Conhecer o Trajeto Percorrido
**Descrição:** Mostrar ao gestor o histórico de trajetos realizados por um veículo.

**Atores:** Gestor da Frota.

### Verificar o Tempo que o Veículo Permaneceu em um Determinado Local
**Descrição:** Identificar o tempo que o veículo ficou estacionado ou parado em um local específico. 

**Atores:** Gestor da Frota.

### Identificar Eventos de Telemetria
**Descrição:** Notificar o gestor sobre eventos importantes, como acelerações bruscas, freadas ou alertas de manutenção preditiva. 

**Atores:** Gestor da Frota.

### Corrigir ou Advertir Motoristas
**Descrição:** Enviar advertências ou notificações ao motorista com base em
comportamentos registrados ou eventos de telemetria. 

**Atores:** Gestor da Frota.

### Especificação de Casos de Uso

### Listar Veículos
**Objetivo:** Visualizar os veículos cadastrados dentro do sistema.

**Atores:** Gestor da Frota.

**Pré-condições:** O usuário deve estar autenticado.

**Fluxo Principal:**

O gestor solicita a listagem de veículos.
O sistema exibe a lista de veículos cadastrados.

**Fluxos Alternativos:**

**A1:** Caso não existam veículos cadastrados, o sistema exibe a mensagem "Nenhum
veículo encontrado".

**Pós-condições:** O gestor visualiza as informações dos veículos cadastrados.

**Critérios de Aceite:** O sistema deve exibir corretamente a lista de veículos
cadastrados, incluindo detalhes como placa, modelo e status.

### Rastrear Veículos
**Objetivo:** Monitorar a localização em tempo real dos veículos da frota.

**Atores:** Gestor da Frota.

**Pré-condições:** O usuário deve estar autenticado no sistema.

**Fluxo Principal:**
O gestor acessa a funcionalidade "Rastrear Veículos".
O sistema exibe um mapa com a localização dos veículos em tempo real.

**Pós-condições:** O gestor consegue visualizar a localização atualizada dos veículos.

**Critérios de Aceite:** O sistema deve permitir que o gestor visualize em tempo real a localização dos veículos no mapa, com atualizações constantes.

### Gerenciar Manutenção
**Objetivo:** Registrar manutenções realizadas e futuras, com notificações preventivas.
Permite a emissão de relatórios detalhados sobre os custos de manutenção da frota.

**Atores:** Gestor da Frota.

**Pré-condições:** O usuário deve estar autenticado.

**Fluxo Principal:**
O gestor acessa a funcionalidade "Gerenciar Manutenção".
O sistema exibe a lista de veículos e suas respectivas manutenções.
O gestor adiciona ou edita um registro de manutenção.
O sistema salva os dados e exibe uma mensagem de sucesso.

**Pós-condições:** O registro de manutenção é atualizado no sistema.

**Critérios de Aceite:** O sistema deve permitir ao gestor registrar, editar e visualizar informações de manutenção de cada veículo.

### Cadastrar Veículo
**Objetivo:** Permitir que o gestor adicione novos veículos à frota no sistema.

**Atores:** Gestor da Frota.

**Pré-condições:** O gestor deve estar autenticado no sistema.

**Fluxo Principal:**
O gestor seleciona a opção "Cadastrar Veículo".
O sistema solicita os dados do veículo (placa, modelo, ano, tipo, dispositivo de
rastreamento).
O gestor insere os dados e confirma.
O sistema salva as informações do veículo na base de dados.
O sistema exibe uma mensagem de sucesso.

**Fluxos Alternativos:**

**A1:** O gestor pode corrigir os dados e reenviar o formulário de cadastro.

**Pós-condições:** O veículo está cadastrado no sistema e pronto para ser gerenciado.

**Critérios de Aceite:** O sistema deve validar os dados inseridos e confirmar o cadastro do veículo.

### Alocar Motoristas
**Objetivo:** Vincular motoristas a veículos para turnos ou viagens.

**Atores:** Gestor da Frota.

**Pré-condições:** O gestor deve estar autenticado no sistema.

**Fluxo Principal:**
O gestor acessa a funcionalidade "Alocar Motoristas".
O sistema exibe a lista de veículos disponíveis.
O gestor seleciona um veículo da lista.
O sistema exibe um formulário para definir o período de alocação.
O gestor insere a data e hora de início e término da alocação.
O gestor confirma a alocação.
O sistema verifica a disponibilidade do veículo e processa a alocação.
O sistema salva os dados e exibe uma mensagem de sucesso.

**Fluxos Alternativos:**

**A1:** Caso o veículo esteja em manutenção ou já alocado, o sistema exibe um alerta.

**Pós-condições:** O veículo está alocado para o período especificado.

**Critérios de Aceite:** O sistema deve validar que o motorista está alocado.

### Verificar a Localização do Veículo
**Objetivo:** Permitir que o gestor visualize a localização atual de um veículo específico.

**Atores:** Gestor da Frota.

**Pré-condições:** O gestor deve estar autenticado no sistema e o veículo deve ter
rastreamento ativo.

**Fluxo Principal:**
O gestor acessa a opção "Verificar Localização".
O sistema exibe o mapa com a localização atual do veículo selecionado.

**Fluxos Alternativos:**

**A1:** O sistema tenta obter a localização após um curto intervalo. o sistema notifica o gestor e sugere verificar a conectividade do rastreador.

**Pós-condições:** A localização do veículo é exibida para o gestor.

**Critérios de Aceite:** O sistema deve exibir corretamente a localização do veículo com base nos dados do rastreamento.

### Conhecer o Trajeto Percorrido
**Objetivo:** Permitir que o gestor visualize o histórico de trajetos realizados por um veículo.

**Atores:** Gestor da Frota.

**Pré-condições:** O veículo deve estar registrado no sistema com o histórico de
rastreamento ativado.

**Fluxo Principal:**
O gestor acessa a opção "Conhecer Trajeto Percorrido".
O sistema exibe o mapa com o trajeto completo do período selecionado.

**Fluxos Alternativos:**

**A1:** Caso não haja dados para o período solicitado, o sistema exibe "Nenhum trajeto disponível".

**Pós-condições:** O trajeto percorrido é exibido ao gestor.

**Critérios de Aceite:** O sistema deve permitir a consulta e exibição do histórico de trajetos conforme o período selecionado pelo gestor.

### Verificar o Tempo que o Veículo Permaneceu em um Determinado Local
**Objetivo:** Identificar o tempo que o veículo ficou parado em um local específico.

**Atores:** Gestor da Frota.

**Pré-condições:** O sistema deve ter dados de localização histórica do veículo.

**Fluxo Principal:**
O gestor acessa a opção "Verificar Tempo em Local".
O sistema exibe o tempo total que o veículo ficou parado no local selecionado.

**Fluxos Alternativos:**

**A1:** Se não houver dados para o local, o sistema exibe "Informação indisponível".

**Pós-condições:** O tempo de parada é exibido.

**Critérios de Aceite:** O sistema deve calcular o tempo com base no veículo parado.

### Identificar Eventos de Telemetria
**Objetivo:** Notificar o gestor sobre eventos como acelerações bruscas ou freadas.

**Atores:** Gestor da Frota.

**Pré-condições:** O veículo deve ter sensores de telemetria instalados e ativos.

**Fluxo Principal:**
O sistema monitora continuamente os sensores de telemetria do veículo.
Quando um evento de telemetria é detectado, o sistema registra os dados do evento.

**Fluxos Alternativos:** 

**A1:** se o sensor estiver desconectado o sistema registra os erros e
exibe um aviso no painel de status do veículo.

**Pós-condições:** O gestor recebe informações sobre o evento registrado.

**Critérios de Aceite:** As notificações devem ser enviadas após o evento.

### Corrigir ou Advertir Motoristas
**Objetivo:** Permitir que o gestor emita advertências ou recomendações corretivas com base nos eventos de telemetria registrados

**Atores:** Gestor da Frota.

**Pré-condições:** o sistema deve ter registrado eventos de telemetria associados a um veículo

**Fluxo Principal:**
O gestor acessa a opção "Gerenciar advertências ".
O sistema exibe uma lista de eventos de telemetria recentes.
O gestor seleciona um evento e visualiza os detalhes.

**Fluxos Alternativos:**

**A1:** se não houver eventos registrados o sistema exibe uma mensagem.

**Pós-condições:** A advertência é registrada no sistema e fica disponível para consulta.

**Critérios de Aceite:** o sistema deve permitir que o gestor emita advertências corretivas de maneira precisa. 

### visualizar historico de localização
**Objetivo** Permitir que o gestor visualize o historico de localização de um veículo dentro de um periodo especificado

**Atores** Gestor da Frota

**Pré-condições** o veículo deve estar registrado no sistema e possuir rastreamento ativo

**Fluxo Principal**
O gestor acessa a funcionalidade "Historico de Localização"
O sistema solicita que o gestor selecione um veículo e defina um período de tempo
O gestor insere os filtros e confirma a busca
O sistema recupera e exibe o Histórico de localização do veículo no período selecionado
O  sistema permite ao gestor visualizar os pontos de localização no mapa ou em formato de relatório

**Fluxos Alternativos**

**A1:** o sistema exibe a mensagem "nenhum dado disponível para este período" caso não tenha dados disponíveis

**Pós-condições**
O histórico de localização do veículo é apresentado ao gestor conforme os critérios selecionados.

**Críterios de Aceite**
O sistema deve exibir corretamente o histórico de localização do veículo.
