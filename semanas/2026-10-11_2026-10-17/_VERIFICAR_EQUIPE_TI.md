# ✅ Verificações da Equipe de TI: semana de 18/10 a 24/10/2026

> Lista de trabalho para Liomar, Isac e David durante a semana, montada a partir do feedback da semana 41 (`../2026-10-04_2026-10-10/feedback.md`) e da análise das fontes da semana 42 (`fontes/**/_ANALISE_*.md`). **Não é fonte do relatório.** O que for feito aqui deve gerar protocolo no Voalle, para aparecer no próximo relatório.
> Problemas das exportações do AutoTickets estão em [`_PENDENCIAS_AUTOTICKETS.md`](_PENDENCIAS_AUTOTICKETS.md).

## 👥 Toda a equipe

- [ ] **Fechar os relatos e pausar o play no fim do expediente.** Também pausar sempre que estiver com foco real em outra atividade. É uma orientação do Isvi para que os apontamentos reflitam a jornada real e para reduzir sobreposições. Na semana 42 houve apontamentos de 120h e 90h (ver Liomar abaixo).
- [ ] **Gincana de segurança (pentest), proposta do Isvi:**
  - Decidir se será feita individualmente ou em grupo e **abrir os protocolos** antes de começar.
  - Cada um pode usar **até 9h** de expediente na semana.
  - Primeiro alvo: **compras.teninternet.com.br**, o sistema de Daniel envolvido no incidente do protocolo 3218766.
  - Entregar um relatório à parte, com falhas encontradas, nível de risco, correções e melhorias sugeridas. Salvar em `semanas/2026-10-18_2026-10-24/fontes/investigacoes/AAAA-MM-DD_pentest_compras/`. O semanal traz a descrição da tarefa e o resumo.
  - Próximas rodadas, um sistema por vez, conforme o Isvi indicar: sistemas do Isvi, outro de Daniel, Ciclos (Edriano) e depois os de terceiros (Voalle, PliQ, Fortics, Power BIs).
- [ ] **Credenciais fora dos relatos:** não registrar senhas em relatos do Voalle; usar o cofre de senhas e citar só a referência. Na semana 42 apareceram senhas de Wi-Fi de cliente, Unifi e Mikrotik em relatos do Isac.
- [ ] **Todo apoio ao técnico de campo com protocolo,** inclusive verificações rápidas em sistema (lição permanente da Coordenação).

## Liomar

- [ ] **Corrigir ou justificar no Voalle** os apontamentos **3217119** (iniciado em 08/10 08:29, **120:09**) e **3218766** (iniciado em 09/10 15:03, **89:37**). Eles ficaram abertos por dias e distorcem o confronto Voalle × Pontomais (tópico 2.4).
- [ ] **⚠️ Slack × AutoTickets (pendência com marca de atenção):**
  - Adiantar o armazenamento seguro do histórico: arquivo criptografado, retenção por tempo indeterminado e acesso só com **MFA simultâneo de 3 entre 6 responsáveis** (TI, Isvi, Edriano – COO, Saulo – CEO, RH e DP).
  - Reunião de acompanhamento de escopo no **fim do mês**.
  - O alinhamento LGPD do #3210508 continua valendo.
- [ ] **Incidente de credenciais e vulnerabilidade no sistema de Compras (3218766):** registrar a continuidade e o desdobramento na gincana.
- [ ] **Protocolo 3218356 (documentos institucionais com o RH):** acompanhar. O Isvi refaz a descrição dos cargos do TI para validar com o RH até o **fim de novembro**.
- [ ] **AutoTickets:** tratar os itens P1 de [`_PENDENCIAS_AUTOTICKETS.md`](_PENDENCIAS_AUTOTICKETS.md):
  - "Tempo Atendimento" de 20670 dias;
  - verificações automáticas de inadimplência paradas desde 06/10;
  - regra do Fullcam incluindo contrato sem câmera.
- [ ] **Exportação do Voalle para o próximo relatório:** HTML, **"Tipo de data: Lançamento"**, um arquivo por colaborador. Não é preciso exportar PDF nem "Inclusão".
- [ ] **Anomalias PPPoE:** gerar o relatório **no dia da emissão do consolidado** e encaminhar ao Service Desk os casos da seção abaixo, com protocolo.

## Isac

- [ ] **3221254:** 4 apontamentos criados em 14/10 às 09:20, 09:21, 09:22 e 09:23, **sem data de fim** e com 00:00. Verificar se são cliques repetidos no play ou apontamentos esquecidos, e encerrar ou remover.
- [ ] **Remover as senhas dos relatos** do 3221804 e do relato "Rede VITU" no Voalle e passá-las ao cofre.
- [ ] **Backups (tópico 8.2):** o quadrante do relatório da semana 41 **não tinha fonte** (24 instâncias e 168 jobs = 24 × 7). Para o próximo relatório, exportar ou capturar do Proxmox/PBS os dados abaixo e salvar em `semanas/2026-10-18_2026-10-24/fontes/infraestrutura/backups/`:
  1. VMs/CTs na rotina;
  2. jobs executados × falhas na semana;
  3. jobs refeitos manualmente e a causa;
  4. data do último teste de restauração.
- [ ] **Teste de restauração:** propor a rotina de 1 a 2 VMs por mês, em rodízio (orientação secundária do Isvi).
- [ ] **Telefonia fixa (prioridade principal da Coordenação):** registrar o status e a evolução da semana.

## David

- [ ] **Frota:** registrar **cada** ocorrência com data, protocolo da requisição, horário combinado × horário liberado e impacto (visita adiada, tempo perdido). O Isvi levou o problema ao Edriano (COO), e Frota fica em Suprimentos e Logística. O registro sustenta essa tratativa.
- [ ] **Wazuh/VPN:** status das 5 filiais com prazo de 26/10 (relatório da semana 41), com percentual e novo prazo se mudar.
- [ ] **Windows 10 × 11:** padrão para novas instalações e situação das licenças.
- [ ] **Contrato 96660 (DAVID BRASIL FERNANDES) no Fullcam:** aparece na auditoria financeira sem ser de câmera. **Não é ação do David**; é um erro do módulo, e o registro deve ser ignorado nos relatórios até a correção (ver AutoTickets).

## Verificações de dados no Voalle (quem estiver com a demanda)

- [ ] **Protocolo 3306821:** citado na análise de acompanhamento de protocolos, com numeração fora da sequência. Confirmar se existe ou se é erro da IA.
- [ ] **Protocolo 3198228 (instalação Fullcam, contrato interno 85854):** preso na fila desde 20/09 com "Nenhuma câmera localizada no FullCam", a cada 2h. Corrigir o cadastro ou encerrar.
- [ ] **Pendências de outros setores** (`fontes/autotickets/acompanhamento_protocolos/`):
  - ar-condicionado do DC-Chácara (14/10);
  - câmeras offline em POPs (Pedras Altas, Angico, Torre do Cruzeiro);
  - nobreaks NHS;
  - status real das 10 câmeras compradas (pergunta do Isvi na semana 40).

## 📡 Encaminhar ao Service Desk: anomalias PPPoE (retrato de 19/10/2026 22:07)

> Hipóteses a confirmar, não fatos. Fonte: `fontes/autotickets/anomalias_pppoe/` (IP no PDF). Gerar novo retrato antes de encaminhar, porque a situação muda.

| Prioridade | Login | Cliente | Contrato | Cidade / POP | MAC | Razão Up/Down | Quedas | RX | Hipótese → ação |
| :-: | :--- | :--- | :--- | :--- | :--- | :-: | :-: | :--- | :--- |
| 1 | nelmasantos_3 | Nelma de Souza Santos | 87971 | Capim Grosso / CG-C3 | 18:81:ed:1f:8c:ef | 47,17x | 3 | −14,69 | CPE comprometida? Verificar CPE, firmware, senha e portas |
| 1 | inailderocha | Inailde de Oliveira Rocha | 67976 | Jacobina / JA-V1 | 70:cd:91:94:86:00 | 42,13x | 1 | −22,29 | 614 GB de upload num plano de 90 Mb. Idem |
| 1 | carlossouza_6 | Carlos Antonio Gomes de Souza | 64388 | Serrolândia / SR-C2 | 70:cd:91:9e:c7:64 | 32,23x | 5 | −20,27 | Idem |
| 1 | reinasl | Reinacy Araujo dos Santos Souza | 10033 | (sem cidade) / SL-C2 | 18:81:ed:37:86:c4 | 19,59x | 3 | −19,39 | Idem. Cadastro sem cidade |
| 1 | jadersantos_1 | Jader Jainer Santana dos Santos | 89883 | Jacobina / OLT JUNCO | 18:81:ed:7c:71:11 | 18,20x | 3 | −19,55 | Idem |
| 2 | josefilho_34 | José Braz Marques Filho | 100993 | Quixabeira / OLT VARZEA DO CANTO | 70:cd:91:9f:6c:54 | 16,94x | 1 | −26,02 | Idem. RX no limite |
| 2 | mariafb | Maria de Fatima Bispo | 26179 | Jacobina / JA-V1 | 70:cd:91:9f:74:78 | 16,15x | 1 | −22,22 | Idem |
| 2 | thiagonascimento_1 | Thiago da Silva Nascimento | 99617 | Várzea do Poço / OLT VÁRZEA DO POÇO | 18:81:ed:32:f1:29 | 9,60x | 10 | **−40** | Sinal crítico/LOS com 10 quedas → **OS de campo** |
| 2 | mailsoncruz | Mailson Gabriel Cruz | 47558 | Ourolândia / OLT OUROLANDIA-DATACOM | 50:d4:f7:d6:e6:f3 | 5,16x | **28** | N/D | Flapping → **OS de campo** |
| 2 | wilsonjunior_2 | Wilson Lima Barros Junior | 89224 | Várzea do Poço / OLT-ITAPURA | 90:9a:4a:02:94:af | 1,07x | **20** | −19,47 | Flapping e rajadas → OS de campo |
| 3 | nathaliavieira_1 | Nathalia Paixão Silva Vieira | 82441 | Serrolândia / SR-C2 | 70:cd:91:f6:f6:8b | 9,44x | 8 | −18,42 | Instabilidade. Verificar CPE e rede interna |
| 3 | rodrigopinho_2 | Rodrigo Bezerra Pinho | 102704 | Jacobina / JA-V1 | 18:81:ed:91:e9:9c | 3,35x | 8 | −19,07 | Instabilidade |
| 3 | 1068.megapix | Megapix Provedor de Internet Ltda | 94549 | Pindobaçu | f4:1e:57:6b:9e:be | 7,99x | 1 | N/A | Provedor como cliente → **Comercial** (possível revenda) |
| — | escritoriocaldeirao | Ten Internet Ltda (cortesia) | 00900 | Caldeirão Grande / SR-C2 | 64:d1:54:a9:93:36 | 5,97x | 1 | N/D | **Contrato interno**: confirmar o uso, não é cliente |

**Cruzamento com a reincidência** (`fontes/autotickets/problemas_recorrentes/`; confirmar pelo contrato, porque o casamento foi feito por nome): **nelmasantos_3** voltou com "Alteração de Senha do Wi-Fi", o que reforça a hipótese de CPE comprometida. **mariafb** e **antoniogoncalves_2** voltaram com "Conexão Lenta".

**Concentração:** o POP **SR-C2** (Serrolândia/Caldeirão Grande) tem 4 casos, e **JA-V1** (Jacobina) tem 3. Vale verificar se há causa comum no POP.
