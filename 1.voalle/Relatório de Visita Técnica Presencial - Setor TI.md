# Relatório de Visita Técnica Presencial - Setor TI

**ÍNDICE**

### Objetivo

Registrar todos os protocolos de visita técnica presencial realizadas pela equipe de TI e que houveram necessidade de utilização de veículo, para verificar 

### Resumo

### Protocolos

#### Junho / 2026

<aside>
⚠️

#### Protocolo [3113236](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3113236) - **30/06/2026 - David Brasil**

**Requerente**: Ramisla Trabuco - Comercial - Capim Grosso

**Veículo / Protocolo**: Palio Branco / Sem protocolo (visita não programada)

**Problema / motivo**: O computador tinha apenas 4GB de memória RAM.

**Solução**: 

Foi realizada a análise do equipamento e identificado que ele possui apenas 4 GB de memória RAM. Após verificação no estoque do TI, foi localizada uma memória DDR4 de 4 GB disponível para instalação, possibilitando que o equipamento fique com 8 GB de memória RAM.

**Observações / Alertas**: 

Ao pegar o veículo no setor de frotas foi disponibilizado um Fiat Palio (branco / 2 portas), onde o mesmo estava com problemas no freio e desalinhado. O motivo da escolha, segundo o gestor do Frota, era porque o atendimento era na sede e porque não havia outro veículo disponível no momento.

</aside>

#### Julho / 2026

<aside>
⚠️

#### Protocolo [3116346](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3116346) - 01/07/2026 - David Brasil

**Requerente**: Ramisla Trabuco - Comercial - Capim Grosso

**Veículo / Protocolo**: Palio Branco / Protocolo [3116624](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3116624)

**Problema / motivo**: Computador preso na tela da BIOS.

**Solução:** Feita troca de posição das memórias RAM.

**Observações / Alertas**: Mesma ressalva do dia anterior, mesmo carro (protocolo 3113236).

</aside>

<aside>
⚠️

#### Protocolo [3117278](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3117278) - 03/07/2026 - David Brasil / Isac Costa

**Requerente**: Setor TI (Proativo) e Geisa Maira (Taquarendi)

**Veículo / Protocolo**: VW Polo / Protocolo 3116745

**Problema / motivo**: Configurar impressora, verificar configurações e melhorias de computador de mesa e recolher notebook temporário. 

**Solução:** 

Foi realizada a atualização do sistema operacional do desktop, substituindo o Windows 7 por um sistema mais atual, além da instalação e configuração dos programas AnyDesk e ChatSeguro. Após a atualização, o equipamento apresentou melhora significativa no desempenho e passou a funcionar de forma satisfatória.

Também foi realizada manutenção preventiva no desktop, incluindo limpeza interna dos componentes, remoção de resíduos e troca da pasta térmica do processador. Foi instalado um nobreak para proteção e continuidade do funcionamento do equipamento.

A impressora foi configurada e testada, porém não ficou totalmente operacional devido à falta das tintas amarela (Yellow), azul/ciano (Cyan) e magenta. O notebook que estava no local foi recolhido, conforme solicitado por Geisa Maira, permanecendo o desktop disponível para utilização no setor.

**Observações / Alertas:** 

O carro foi agendado com dois dias de antecedência, mas não havia carro disponível no momento da retirada. Roseval verificou com Genímedes se havia carro disponível das equipes dele e foi disponibilizado o carro de utilização de Henrique, que estava de folga no dia.

</aside>

<aside>
⚠️

#### Protocolo [3124836](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3124836) - 09/07/2026 - David Brasil

**Requerente**: Mariana Ferreira - Comercial - Capim Grosso

**Veículo / Protocolo**: Veículo próprio (pessoal)

**Problema / motivo:** Memória com 90% de utilização, resultando em travamentos no notebook.

**Solução:** 

Desabilitada inicialização de aplicativos desnecessários. Após isso, o consumo de memória caiu para entre 74% ~ 76%. Não foi necessário upgrade, pois o mesmo já possui 8GB.

**Observações / Alertas:** 

</aside>

<aside>
⚠️

#### Protocolo 3129316 (Liomar), Protocolo 3129380 (Isac) - 13/07/2026

**Protocolo de origem**: **3124344**

**Requerente**: 

**Problema**: Realizar resolução de problemas in loco e análise técnica para upgrade de equipamentos na residência da cliente Danielle.

**Solução:** 

A equipe técnica (Liomar, Isac, Vitor e João Paulo) identificou falhas de topologia e configuração nos equipamentos Datacom da residência (1 ONT DM986-416 AX30 HW2 e 2 roteadores secundários DM956-4GT 3000). Foram constatadas inconsistências nos nomes das redes (SSIDs) entre as bandas 2.4 GHz e 5 GHz, cabeamento em porta LAN em vez da porta WAN padrão e a função Mesh desativando-se de forma autônoma.

Optou-se por desativar a função Mesh devido ao histórico de falhas da fabricante, priorizando o roaming nativo das redes sem fio (Wi-Fi 6 em 160 MHz e Wi-Fi 4 em 20 MHz). A ONT e os roteadores secundários (configurados com WAN em bridge e DHCP Client) foram padronizados com os mesmos SSIDs. Os testes de estresse validaram o roaming (troca aos 75 dBm) e entregaram taxas de download no Wi-Fi variando entre 650 Mbps (c/ obstáculos) e 1.136 Mbps.

Será aberto um protocolo junto ao setor Comercial para monitoramento da estabilidade da rede por um período de uma a duas semanas. Caso a cliente reporte novos problemas, será ofertado o upgrade para a seguinte infraestrutura corporativa:

- 1x Mikrotik RB750Gr3 + ONU independente (área da churrasqueira).
- 1x Grandstream GWN7660 (teto da academia).
- 1x Grandstream GWN7660 (porta da sala no térreo).
- Manutenção do roteador Datacom no escritório como ponto de acesso complementar, se comprovada deficiência de cobertura no andar superior.

**Observações / Alertas**: 

Aberto Protocolo 3132491 (oportunidade de negócio) da viabilidade técnica realizada (conforme orientado por Naila), com a sugestão de upgrade caso a cliente volte a reclamar nas próximas semanas. Informado à Naila (Comercial) sobre o caso.

</aside>

<aside>
⚠️

#### Protocolo [3127431](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3124836) - 14/07/2026 - David Brasil

**Requerente**: Larissa Roza / Cobrança

**Veículo / Protocolo**: Moto / Sem protocolo (visita não programada)

**Problema / motivo:** Monitor da colaboradora Marilucia não estava ligando. A CPU aparentemente estava normal, mas o monitor não ligava.

**Solução:** 

Ao chegar no local, o computador já estava funcionando normalmente. Ao procurar o motivo do problema, vi que o cabo de força estava relativamente frouxo no nobreak. Larissa informou que, também, o computador já vinha apresentando sinais de lentidão além de reforçar sobre o desligamento e informou ter outro desktop sem uso disponível. Com isso, coloquei o SSD do PC atual no outro desktop e reforcei a ligação do cabo de força no nobreak. O computador de Marilucia foi colocado no lugar do outro, que era de uma colaboradora que foi desligada.

**Observações / Alertas:** 

</aside>

<aside>
⚠️

#### Protocolos [3128243](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3128243) (Cobrança) e [3128711](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3128711) (Dep. Pessoal) - David Brasil - 15/07/2026

**Veículo / Protocolo**: Moto / Sem protocolo (visita não programada)

**Requerente**: 

- Larissa Roza - Cobrança - Capim Grosso
- Jeferson Gonçalves - Departamento Pessoal - Capim Grosso

**Problema / motivo:** 

- Cobrança: Problema de acesso ao Sistema LEMIT em vários computadores (Setor Cobrança).
- Dep. Pessoal: Problema no ramal do setor.

**Solução:** 

- Cobrança: Para resolver o problema de acesso ao LEMIT foi desabilitado o protocolo IPv6 das máquinas que iriam utilizar, assim abriu normalmente (liberação do sistema é através do IP público e o sistema, ao sair pelo IPv6, acusava como acesso não permitido).
- Dep. Pessoal: Só havia 1 ramal para todo o setor. Foi realizada a criação dos ramais de Patrícia (ramal 566) e Jefferson (ramal 491) no sistema Native PBX. Após isso, foi realizada a instalação do sofware MicroSIP nos computadores de Patrícia e de Jefferson.

**Observações / Alertas:** 

</aside>

<aside>
⚠️

#### Protocolo 3129281 (Liomar) e Protocolo 3129308 (Isac) - 15/07/2026

**Protocolo de origem**: 3123655

**Veículo / Protocolo**: VW Saveiro (cedida por Emerson)

**Requerente**: Saulo Xavier - Equipe Técnica - Santaluz

**Problema / motivo**: Realizar viabilidade técnica para os eventos que ocorrerão nos dias 18/07 (Paredão) e entre os dias 24/07 e 27/07 (Aniversário da Cidade).

**Solução**: 

#### 1. Evento: Praça de Misso - Paredão (18 e 19/07)

**Requisitos de Hardware e Topologia:**

- **Access Points:** 3x Grandstream 7664LR.
- **Roteamento Core:** 1x MikroTik CCR1036.

#### 2. Evento: Aniversário de Santaluz (24 a 27/07)

**Equipamentos (resumido):**

- **4x Huawei AirEngine 6760R-51E**
- **1x Mikrotik CCR 1009 (Huawei)**
- **1x Mikrotik CCR 1036 ou CCR 1009**
- **4x Grandstream GWN 7664LR**
- **4x Roteadores Datacom Wi-Fi 6**

**Requisitos de Hardware e Topologia (Detalhado):**

- **Uplink:** 2x ou 3x Fibras (Atendimento via ONU + 2x PPPoE), segmentadas para as regiões da entrada do Palco e da entrada do Fundo (motivo: grande distância entre a frente e o fundo + alto fluxo de pessoas).
    - PS: Terceira fibra analisar a depender do local que o caminhão do sistema de câmeras vai ficar.
- **Roteamento:** 2x MikroTik CCR (alocadas estrategicamente para Palco (CCR 1009 Huawei) e Fundo (CCR1036 ou CCR1009)).
- **Setor Casa de Saúde:** 2x Roteadores Datacom.
- **Setor Camarim:** 1x Roteador Datacom (cabeamento CCR 1009).
- **Setor Transmissão (Live):** 1x Roteador (cabeamento CCR 1009 ou nova fibra).
- **Setor Palco e Circuito de Barracas:** 4x AP's Huawei AirEngine 6760R-51E.
- **Setor Fundo:** 4x AP's Grandstream GWN 7664LR integrados a 1x Switch PoE.
- **Portal Lateral:** Lançamento de cabo drop exigido para sistema de câmeras.
- **Portal do Fundo:** Lançamento de cabo drop saindo da área do palco e instalação de roteador dedicado para sistema de Câmeras.

**Pontos de Atenção, Validações e Plano de Ação**

- **Logística de Reutilização de Hardware:** A MikroTik CCR1036 e as antenas Grandstream 7664LR que operarão na Praça de Misso (18 e 19/07) são as mesmas que comporão a infraestrutura do Fundo no Aniversário de Santaluz (24 a 27/07).
- **Infraestrutura Elétrica (Circuito de Barracas):** A instalação dos 4 equipamentos Huawei exige a disponibilização prévia de 3 a 4 tomadas elétricas nos postes. É necessário acionar os responsáveis pela elétrica do evento para validar a estabilidade e aterramento desses pontos, mitigando o risco de reinicialização dos equipamentos sob carga.

**Observações / Alertas**: 

</aside>

<aside>
⚠️

#### Protocolo [3129482](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3129482) - David Brasil - 15/07/2026

**Veículo / Protocolo**: Fiat Strada / Protocolo 3127894

**Requerente**: Geiza Maira - Comercial - Várzea da Roça

**Problema / motivo:** Impressora não estava imprimindo e o sistema operacional estava quebrado.

**Solução:** 

Realizei a formatação do computador, instalando o Windows 10. O problema da impressora foi que o contador das almofadinha tinha zerado, então foi necessário baixar um software para resetar o contador da almofadinha, feito isso a impressora voltou a imprimir normalmente.

**Observações / Alertas:** O freio estava mais fraco do que o normal, onde mesmo pisando forte, demorava a reduzir a velocidade.

</aside>

<aside>
⚠️

#### Protocolo [3131378](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3131378) - David Brasil - 17/07/2026

**Veículo / Protocolo**: Fiat Palio Preto / Protocolo 3131370

**Requerente**: Geiza Maira - Comercial - Pereira

**Problema:** O colaborador está reclamando que impressora está se desligando sozinha direto.

**Solução:** 

Desloquei-me até a cidade de Pereira para realizar um atendimento na loja da TEN. Foi feita a formatação do computador e a instalação do Windows 10.
Após a instalação do sistema operacional, instalei o HP Smart e realizei a configuração da impressora. Também foram feitos testes de impressão e digitalização, e ambos funcionaram corretamente.
Por fim, orientei o colaborador Luiz Neto sobre como utilizar a impressora e realizar as digitalizações.

**Observações / Alertas:** 

Carro disponibilizado pelo frota estava com apenas 1 dos pneus liso, desalinhado e com freios não muito eficientes.

</aside>

<aside>
⚠️

#### Protocolo 3138096 (Isac e Liomar) - 24/07/2026

**Veículo / Protocolo**: Fiat Strada

**Requerente**: Saulo Xavier - Equipe Técnica - Santaluz

**Problema / motivo**: Analisar o funcionamento da rede no local do evento, realizar testes e se necessário aplicar configurações para melhora do desempenho.

**Solução**: 

Ao chegarmos no local, os equipamentos da frente e fundo do evento estavam instalados, 2x CCR, 4x Huawei e 4x Grandstream, os Huawei estavam funcionando perfeitamente, porém. o Switch POE que alimentava os grandstream estava conectado com cabo fast, limitando a velocidade dos AP’s em 100Mbps, problema que foi resolvido após troca do cabo/conector deituoso.

Conforme explicação abaixo, caso os técnicos tivessem seguido os protocolos de instalação, que estava errados, e provisionado os equipamentos com o Vtask, os PPPoE’s duplicados causariam a queda de conexão em toda a rede do evento, para evitar a situação, foi necessário que Liomar realizasse o provisionamento de forma manual e reorganizasse os PPPoE’s para atender aos equipamentos.

*Informações protocolos Marketing x equipe técnica*

- 3133856 - Palco Santaluz (camarim) - eventos_santaluz_3 (Mesmo PPPoE da mesa de som!)
- 3133811 - Mesa de som (live) - eventos_santaluz_3
- 3133794 - Mikrotik CCR Huawei Frente + CCR Grandstream - eventos_santaluz_2 (ÚNICO PPPOE PARA 2 MIKROTIKS)

Logins provisionados:

- Mesa de som: eventos_santaluz_3
- Huawei frente: eventos_santaluz_1
- Grandstream Fundo: eventos_santaluz_2
- Camarote: eventos_59, eventos_59
- Camarim: eventos_65, 102030

---

Camarim: ONT WI-FI 6

Nome Wi-Fi: "TEN-CAMARIM", "TEN-CAMARIM-5G"

Senha: Camarim@luz2026

MESA DE SOM: ONT WI-FI 6:

Nome Wi-Fi: SANTALUZ_TEN_LIVE e SANTALUZ_TEN_5G

Senha: Live@luz2026

MONIT. CAMERAS REC. FACIAL: ONT WI-FI 6

Nome Wi-Fi: TEN_POLICIAMENTO e TEN_POLICIAMENTO_5G

Senha: Adm@luz2026

BILHETERIA E CAMAROTE: CCR + 3X 7664ELR

Bilheteria apenas:

Nome Wi-Fi: TEN-BILHETERIA e TEN-BILHETERIA-5G

Senha: santaluz2026

WI-FI HOTSPOT VOUCHER: TEN_HANGAR_LIVRE

Camarote apenas:

Nome Wi-Fi: TEN_Hangar_Lounge

Senha: hangar2026

REDE PALCO FRENTE: CCR + 4X HUAWEI

Nome Wi-Fi: SANTALUZ_TEN e SANTALUZ_TEN_5G

Senha: adm@luz2026

REDE FUNDO: CCR + 4X GRANDSTREAM GWN7664LR

Hotspot: TEN_Wi-Fi, hotspot normal cliente + não sou cliente

Nome Wi-Fi: SANTALUZ_TEN (2.4 e 5G)

Senha: adm@luz2026

**Observações / Alertas**: Devido a falta de pessoas e o aumento da demanda no local do evento, tivemos que ficar para ajudar nas instalações e configurações de equipamentos em vários pontos do espaço, a pedido de Saulo Xavier, finalizando os trabalhos por volta das 22h.

</aside>

<aside>
⚠️

#### Protocolo [3139144](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3139144), [3139036](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3139036) e [3139924](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3139924) - David Brasil - 27/07/2026

**Veículo / Protocolo**: Moto CG FAN / Protocolo 3131370

**Requerentes**: Larissa Roza, Isa Costa e Allana Pimentel - Capim Grosso

**Problema:** 

**1. Substituição de nobreak no Controle de Qualidade:**
Necessidade de instalação de um novo nobreak na estação de trabalho da colaboradora Laiana (setor de Qualidade), devido à falha de bateria do equipamento antigo.

**2. Validação de hardware para nova colaboradora:**
Solicitação de inspeção técnica e verificação de integridade de um computador em estoque (Patrimônio: 001273), com o objetivo de preparar a estação de trabalho para a nova estagiária.

**3. Falha de acionamento (botão emperrado) na unidade Capim Grosso:**
O computador da atendente Bianca não ligava devido a um travamento mecânico e quebra do botão de ligar/desligar (*Power*) no painel frontal do gabinete.

**Solução:** 

**1. Instalação de novo nobreak e encaminhamento de bateria:**
Realizada a instalação e os testes de carga do novo nobreak na estação da colaboradora Laiana, deixando o equipamento operacional. O nobreak antigo foi recolhido e entregue ao setor de Estoque para a substituição da bateria interna.

- *Nota de acompanhamento:* A própria requerente foi orientada a verificar diretamente com o Estoque a conclusão da troca da bateria para posterior devolução ou alocação.

**2. Aprovação de hardware e liberação para uso:**
Realizada inspeção preventiva e teste de desempenho no computador de **Patrimônio 001273**. As especificações técnicas foram validadas:

- **Processador:** AMD A6-9500
- **Memória RAM:** 8 GB
- **Armazenamento:** SSD Lexar de 128 GB
- *Conclusão:* O hardware está em perfeitas condições de funcionamento e desempenho, sendo aprovado e liberado para o uso da nova estagiária.

**3. Limpeza interna e remapeamento de chave de acionamento:**
Executada limpeza preventiva interna para remoção de excesso de poeira no hardware. Para resolver o problema do botão *Power* quebrado sem necessidade de troca imediata do gabinete, foi aplicada uma solução adaptativa técnica no painel frontal da placa-mãe: o conector do botão de **Reset (*Reset SW*)** foi transferido para os pinos de **Ligar (*Power SW*)**. O computador agora é ligado normalmente pelo botão de *Reset*. Teste de acionamento realizado com sucesso e equipamento operacional.

**Observações / Alertas:** 

O baú da moto não tinha cadeado para fechar; por isso, utilizei um arame para fazer a função da trava.

</aside>

#### Agosto / 2026

<aside>
⚠️

#### Protocolo [31](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3139144)[3148140](https://synsuite.teninternet.com.br/attendance#/customer-attendance/3139924) - David Brasil - 03/08/2026

**Veículo / Protocolo**: Moto CG FAN 

**Requerentes**: Isa Costa

**Problema:** 

- **Equipamentos inoperantes:** Alguns computadores não estão ligando (provavelmente porque estão conectados às tomadas da parede sem energia).
- **Falta de conectividade:** Os computadores que continuam ligados não têm acesso à rede/internet. O cabeamento depende da parede afetada, o que indica que os equipamentos de rede (como switches ou roteadores) alocados ali também estão sem energia.

**Solução:** 

Compareci ao local e me dirigi à mesa da requerente para avaliar a situação. Utilizando um multímetro, testei as tomadas e constatei que não havia energia na parede amarela do setor, enquanto o lado oposto funcionava normalmente.

Como o sintoma apontava para uma falha elétrica, tentei acionar o Nildo (responsável pela parte elétrica), mas não obtive retorno. Em seguida, contatei o Jean (responsável pela infraestrutura), que informou que enviaria o Nildo ao local assim que ele retornasse de Jacobina.

Posteriormente, Jean chegou ao setor acompanhado de um técnico. Durante a inspeção, o técnico identificou que o desarme do disjuntor era provocado por uma máquina específica que estava em curto.

O equipamento foi recolhido para o setor de TI. Na bancada, identificamos que a causa raiz do curto-circuito era o cabo de força, que estava fisicamente danificado (imagem em anexo). O cabo foi substituído e, após os testes, a máquina voltou a funcionar normalmente.

**Observações / Alertas:** 

O baú da moto não tinha cadeado para fechar; por isso, utilizei um arame para fazer a função da trava. Devido ser uma urgência tive dificuldades de retirar o veiculo para atender a demanda, o setor estava parado desde 07h:30 e tive que aguardar até as 08h:00 para conseguir tirar o veiculo. 

</aside>