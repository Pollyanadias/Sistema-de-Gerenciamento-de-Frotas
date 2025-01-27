**Sistema de Controle de Frotas: Rastreamento de veículos, manutenção preventiva e alocação de motoristas**

***Levantamento de Requisitos***

Requisitos Funcionais:
Permitir o rastreamento em tempo real da localização dos veículos.
Exibir mapas com trajetos percorridos e informações detalhadas de cada veículo.
Registrar manutenções realizadas e notificar sobre manutenções preventivas.
Gerar relatórios de custos de manutenção.
Vincular motoristas a veículos para viagens ou turnos específicos.
Exibir lista de motoristas e veículos disponíveis para alocação.
Alertar sobre inconsistências, como motoristas sem habilitação válida.
Verificar a localização atual dos veículos.
Saber a velocidade dos veículos.
Conhecer o trajeto percorrido pelos veículos.
Verificar o tempo que os veículos permaneceram em um local específico.
Identificar eventos de telemetria importantes.
Corrigir ou advertir motoristas..


***Requisitos Não Funcionais:***

O rastreamento deve ser atualizado a cada 5 segundos.
O sistema deve ser capaz de gerar relatórios mensais de custos de manutenção.
O sistema deve permitir consultas rápidas de alocações passadas e atuais.
A interface do sistema deve ser intuitiva e responsiva.
O sistema deve suportar até 500 usuários simultâneos.
O sistema deve garantir alta disponibilidade, com tolerância a falhas de até 99,9%.


***Regras de Negócio***

***Autenticação de Usuários:***

Somente usuários autenticados podem acessar as funcionalidades do sistema.
O gestor é o único autorizado a realizar operações administrativas, como cadastro e exclusão de dados.
Cadastro de Veículos:
Todos os veículos devem ser cadastrados com informações completas, incluindo placa, modelo, status e dispositivos de rastreamento.
Veículos sem dispositivos de rastreamento não podem ser incluídos na frota operacional.

***Rastreamento de Veículos:***

O rastreamento deve ocorrer em tempo real com atualizações a cada 5 segundos.
O sistema deve emitir alerta caso algum veículo esteja fora da rota planejada.

***Manutenção Preventiva:***

Manutenções preventivas devem ser registradas com base na quilometragem ou tempo de uso.
Notificações automáticas devem ser enviadas ao gestor antes do vencimento.

***Alocação de Motoristas:***

Apenas motoristas com habilitação válida e documentação atualizada podem ser alocados a veículos.
A alocação deve especificar o período de uso e pode ser modificada apenas pelo gestor.

***Relatórios:***

Relatórios de custos e desempenho devem ser gerados mensalmente.
Todos os relatórios devem estar disponíveis para consulta em até 12 meses após sua geração.

***Segurança dos Dados:***

Os dados sensíveis devem ser protegidos com criptografia.
O sistema deve manter logs de todas as ações realizadas por usuários para auditoria.

***Capacidade de Escalabilidade:***

O sistema deve ser capaz de gerenciar até 500 veículos e 1000 motoristas simultaneamente.


*** Relação de Casos de Uso ***

***Casos de Uso***

***Fazer Login***
**Descrição:** Permitir que os usuários autenticados acessem as funcionalidades do sistema.
**Atores:** Gestor da Frota, Motorista.

***Rastrear Veículos***
**Descrição:** Monitorar a localização em tempo real dos veículos da frota.
**Atores:** Gestor da Frota.

***Gerenciar Manutenção***
**Descrição:** Registrar manutenções realizadas e futuras, com notificações preventivas. Permite a emissão de relatórios detalhados sobre os custos de manutenção da frota.
**Atores:** Gestor da Frota.

***Alocar Motoristas***
**Descrição:** Vincular motoristas a veículos para turnos ou viagens, garantindo que apenas motoristas qualificados sejam alocados.
**Atores:** Gestor da Frota, Motorista.

***Verificar a Localização do Veículo***
**Descrição:** Permitir que o gestor visualize a localização atual de um veículo específico.
**Atores:** Gestor da Frota.

***Saber a Velocidade do Veículo***
**Descrição:** Informar ao gestor a velocidade atual ou média do veículo.
**Atores:** Gestor da Frota.

***Conhecer o Trajeto Percorrido***
**Descrição:** Mostrar ao gestor o histórico de trajetos realizados por um veículo.
**Atores:** Gestor da Frota.

***Verificar o Tempo que o Veículo Permaneceu em um Determinado Local***
**Descrição:** Identificar o tempo que o veículo ficou estacionado ou parado em um local específico.
**Atores:** Gestor da Frota.

***Identificar Eventos de Telemetria***
**Descrição:** Notificar o gestor sobre eventos importantes, como acelerações bruscas, freadas ou alertas de manutenção preditiva.
**Atores:** Gestor da Frota.

***Corrigir ou Advertir Motoristas***
**Descrição:** Enviar advertências ou notificações ao motorista com base em comportamentos registrados ou eventos de telemetria.
**Atores:** Gestor da Frota, Motorista.


***Especificação de Caso de Uso***

**Nome do Sistema:** Sistema de Controle de Frotas.

**Especificação de Casos de Uso**
***Fazer Login***
**Objetivo:** Permitir que os usuários autenticados acessem as funcionalidades do sistema.
**Atores:** Gestor da Frota, Motorista.
**Pré-condições:** O usuário deve estar cadastrado no sistema.
**Fluxo Principal:**
O usuário insere suas credenciais no sistema.
O sistema valida as credenciais.
O acesso é concedido ao usuário.
**Fluxos Alternativos:**
**A1:** Caso o usuário insira credenciais incorretas, o sistema exibe uma mensagem de erro e solicita uma nova tentativa.
**Pós-condições:** O usuário está autenticado e pode acessar as funcionalidades permitidas.
**Critérios de Aceite:** O sistema deve validar credenciais em no máximo 3 segundos.

***Rastrear Veículos***
**Objetivo:** Monitorar a localização em tempo real dos veículos da frota.
**Atores:** Gestor da Frota.
**Pré-condições:** O gestor deve estar autenticado no sistema e os veículos devem ter dispositivos de rastreamento ativos.
**Fluxo Principal:**
O gestor acessa o sistema e seleciona a opção "Rastrear Veículos".
O sistema exibe um mapa com a localização em tempo real dos veículos.
O gestor escolhe um veículo para obter detalhes adicionais.
**Fluxos Alternativos:**
**A1:** Caso o dispositivo de rastreamento de um veículo esteja desconectado, o sistema exibe uma mensagem de alerta.
**Pós-condições:** A localização dos veículos é exibida em tempo real no mapa.
**Critérios de Aceite:** O sistema deve atualizar a localização a cada 5 segundos.

***Gerenciar Manutenção***
**Objetivo:** Registrar manutenções realizadas e futuras, com notificações preventivas.
**Atores:** Gestor da Frota.
**Pré-condições:** O gestor deve estar autenticado no sistema.
**Fluxo Principal:**
O gestor seleciona "Gerenciar Manutenções".
O sistema exibe a lista de veículos e suas condições de manutenção.
O gestor registra uma manutenção ou programa uma nova.
O sistema salva os dados e atualiza o status do veículo.
**Fluxos Alternativos:**
**A1:** Caso o registro falhe, o sistema solicita ao gestor que tente novamente.
**Pós-condições:** As informações de manutenção são registradas e notificadas conforme programado.
**Critérios de Aceite:** O sistema deve emitir notificações preventivas com 48 horas de antecedência.

***Alocar Motoristas***
**Objetivo:** Vincular motoristas a veículos para turnos ou viagens.
**Atores:** Gestor da Frota, Motorista.
**Pré-condições:** O gestor deve estar autenticado no sistema, e o motorista deve estar cadastrado com documentação válida.
**Fluxo Principal:**
O gestor seleciona "Alocar Motoristas".
O sistema exibe a lista de motoristas e veículos disponíveis.
O gestor vincula um motorista a um veículo para um período específico.
O sistema salva a alocação.
**Fluxos Alternativos:**
**A1:** Caso o motorista não possua habilitação válida, o sistema exibe um alerta.
**Pós-condições:** O motorista está vinculado ao veículo e o registro está atualizado.
**Critérios de Aceite:** O sistema deve validar a documentação do motorista antes da alocação.
Verificar a Localização do Veículo
**Objetivo:** Permitir que o gestor visualize a localização atual de um veículo específico.
**Atores:** Gestor da Frota.
**Pré-condições:** O gestor deve estar autenticado no sistema e o veículo deve ter rastreamento ativo.
**Fluxo Principal:**
O gestor acessa a opção "Verificar Localização".
O sistema exibe o mapa com a localização atual do veículo selecionado.
**Fluxos Alternativos:**
**A1:** Se o dispositivo de rastreamento não responder, o sistema exibe uma mensagem de erro.
**Pós-condições:** A localização do veículo é exibida para o gestor.
**Critérios de Aceite:** O sistema deve atualizar as informações de localização em tempo real.

***Saber a Velocidade do Veículo***
**Objetivo:** Informar ao gestor a velocidade atual ou média de um veículo.
**Atores:** Gestor da Frota.
**Pré-condições:** O veículo deve estar em movimento e o rastreamento ativo.
**Fluxo Principal:**
O gestor seleciona "Saber Velocidade" no sistema.
O sistema exibe a velocidade atual do veículo.
**Fluxos Alternativos:**
**A1:** Se o veículo estiver parado, o sistema exibe a mensagem "Veículo parado".
**Pós-condições:** A velocidade é exibida ao gestor.
**Critérios de Aceite:** As informações de velocidade devem ser precisas e atualizadas em tempo real.

***Conhecer o Trajeto Percorrido***
**Objetivo:** Permitir que o gestor visualize o histórico de trajetos realizados por um veículo.
**Atores:** Gestor da Frota.
**Pré-condições:** O veículo deve estar registrado no sistema com o histórico de rastreamento ativado.
**Fluxo Principal:**
O gestor acessa a opção "Conhecer Trajeto Percorrido".
O sistema exibe o mapa com o trajeto completo do período selecionado.
**Fluxos Alternativos:**
**A1:** Caso não haja dados para o período solicitado, o sistema exibe "Nenhum trajeto disponível".
**Pós-condições:** O trajeto percorrido é exibido ao gestor.
**Critérios de Aceite:** O sistema deve mostrar trajetos de até 30 dias no histórico.

***Verificar o Tempo que o Veículo Permaneceu em um Determinado Local***
**Objetivo:** Identificar o tempo que o veículo ficou parado em um local específico.
**Atores:** Gestor da Frota.
**Pré-condições:** O sistema deve ter dados de localização histórica do veículo.
**Fluxo Principal:**
O gestor acessa a opção "Verificar Tempo em Local".
O sistema exibe o tempo total que o veículo ficou parado no local selecionado.
**Fluxos Alternativos:**
**A1:** Se não houver dados para o local, o sistema exibe "Informação indisponível".
**Pós-condições:** O tempo de parada é exibido.
**Critérios de Aceite:** O sistema deve calcular o tempo com precisão de minutos.

**Identificar Eventos de Telemetria**
**Objetivo:** Notificar o gestor sobre eventos como acelerações bruscas ou freadas.
**Atores:** Gestor da Frota.
**Pré-condições:** O veículo deve ter sensores de telemetria instalados e ativos.
**Fluxo Principal:**
O sistema monitora em tempo real os sensores do veículo.
Ao identificar um evento, o sistema notifica o gestor.
**Fluxos Alternativos:**
**A1:** Se o sensor estiver desconectado, o sistema emite um alerta de falha.
**Pós-condições:** O gestor recebe informações sobre o evento registrado.
**Critérios de Aceite:** As notificações devem ser enviadas em até 10 segundos após o evento.

***Corrigir ou Advertir Motoristas***
**Objetivo:** Permitir que o gestor envie advertências ou notificações ao motorista com base em eventos registrados.
**Atores:** Gestor da Frota, Motorista.
**Pré-condições:** O motorista deve estar cadastrado e ativo no sistema.
**Fluxo Principal:**
O gestor acessa a opção "Corrigir Motorista".
O sistema exibe a lista de eventos relacionados ao motorista.
O gestor seleciona um evento e envia uma advertência.
**Fluxos Alternativos:**
**A1:** Se o motorista não estiver disponível no sistema, o sistema exibe "Motorista não encontrado".
**Pós-condições:** A advertência é enviada ao motorista.
**Critérios de Aceite:** As notificações devem ser entregues em até 5 segundos.

