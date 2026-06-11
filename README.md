# FASE-7
Consolidação de tecnologias

Como a fase 7 é apra a consolidação das tecnologias e atividades realizadas, fora preciso aplicar mudanças significativas em algumas atividades para que fosse preciso unificar todas as fases; inicialmente tive um pouco de dificuldade em realizar a atividade 5 relacionada ao armazenamento das fases na nuvem, pois a mesma não foi exigida nas aulas, inclusive foi informado em uma das aulas que não precisariamos ciar nenhum repositorio na nuvem.

Fase 1: Consolidação da base de dados estruturada através da modelagem de áreas de plantio e otimização do manejo de insumos. Essa estrutura serve como camada de ingestão para o ecossistema digital, viabilizando a análise estatística descritiva e inferencial dos dados via linguagem R.

Fase 2 – Persistência e Estruturação de Dados: Desenvolvimento da arquitetura de dados relacional por meio da elaboração dos Modelos Entidade-Relacionamento (MER) e Conceitual/Lógico (DER). Esta estrutura realiza a ingestão e unificação dos dados de manejo agrícola originados na Fase 1, garantindo consistência transacional e integridade referencial para suportar análises analíticas futuras.

Fase 3 – Sistemas Embarcados e Automação: Desenvolvimento de um ecossistema IoT baseado no microcontrolador ESP32 para automação de irrigação. O firmware executa uma lógica de controle retroalimentada que aciona os atuadores (bombas d'água) a partir da leitura de sensores de umidade (DHT22) e parâmetros físico-químicos (pH e nutrientes simulados via transdução/LDR). A persistência dos dados e o histórico de telemetria são gerenciados por meio de operações CRUD diretas na camada de banco de dados estruturada na Fase 2.

Fase 4 – Inteligência de Dados e Interfaces de Monitoramento: Desenvolvimento de uma plataforma preditiva bifásica para suporte à tomada de decisão. Na camada de nuvem, implementou-se um dashboard interativo via Streamlit, integrando modelos de Machine Learning (Scikit-Learn) para predição de demandas de irrigação e manejo. Na camada de borda (edge), o ESP32 realiza o monitoramento local e analógico em tempo real através de um display LCD e do Serial Plotter, garantindo redundância visual das métricas críticas de campo.

Fase 5 – Infraestrutura em Nuvem e Segurança da Informação: Provisionamento de toda a infraestrutura do ecossistema na plataforma AWS, adotando uma arquitetura escalável, resiliente e de alta disponibilidade. A governança e a segurança dos dados de telemetria foram desenhadas em conformidade com as diretrizes das normas ISO/IEC 27001 e 27002, implementando segregação de acessos (através de políticas de IAM), criptografia de dados em repouso e em trânsito, e isolamento de rede para mitigar vulnerabilidades e proteger ativos sensíveis.

Fase 6 – Visão Computacional e Redes Neurais Convolucionais: Desenvolvimento de um sistema de monitoramento baseado na arquitetura YOLO (Análise de Alvos em Tempo Real) para a detecção 

Fase 7 - Arquitetura do Serviço de Alerta (AWS)

Origem dos Dados: Os scripts das Fases 1, 3 ou 6 (rodando no VS Code ou simulados) enviam os dados para a AWS.

Processamento (AWS Lambda): Uma função analisa se os valores dos sensores ultrapassaram os limites seguros.

Notificação (Amazon SNS): Se um limite for atingido, o SNS dispara um SMS ou E-mail com a ação corretiva pré-definida.

## 🚀 Serviço de Mensageria e Alertas (Fase Final)

Para garantir a segurança e a tomada de decisão rápida na fazenda, implementamos um sistema de alerta automatizado utilizando a infraestrutura da AWS. O sistema monitora os dados coletados e envia notificações em tempo real (E-mail/SMS) para os funcionários com ações corretivas.

### 1. Configuração do Amazon SNS (Simple Notification Service)

* Criamos um **Tópico** no Amazon SNS do tipo *Standard* chamado `Alertas_Fazenda`.
* Criamos duas **Assinaturas (Subscriptions)**: uma do tipo `Email` e outra do tipo `SMS`, apontando para os contatos dos operadores responsáveis.


### 2. Criação da Função AWS Lambda

* Desenvolvemos uma função Lambda em Python que recebe a leitura do sensor, valida as regras de negócio das Fases 1, 3 e 6, e define a ação corretiva necessária.

automatizada animais e flores. O pipeline de processamento foi projetado de forma modular: embora compatível com a ingestão dedados em borda via hardware embarcado (ESP32-CAM), a validação e o desdobramento do modelo foram consolidados através de um dataset local de imagens estáticas de alta resolução, otimizando a acurácia do algoritmo de detecção.
