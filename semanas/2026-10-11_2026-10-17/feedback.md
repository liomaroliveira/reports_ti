# Feedback e Observações — Relatório da Semana 41 (04/10 a 10/10/2026)

<!-- Observações sobre o relatório da semana 41. Lidas na geração da semana 42; cada item precisa ser tratado.
     (Conteúdo preenchido originalmente em templates/feedback.md no commit ce4e27a e movido para cá.) -->
<!--
  Copie este arquivo para a pasta da semana AVALIADA (a do relatório que recebeu o feedback):
    cp templates/feedback.md semanas/<semana-avaliada>/feedback.md
  O relatório da semana seguinte lê este arquivo e trata cada observação (Resumo Executivo + tópico correspondente).
  Escreva uma observação por item. Pode colar o texto do Isvi como veio (WhatsApp, e-mail, Slack).
-->

## Isvi Neemias (Coordenação)

### Correções



### Perguntas



### Orientações e outros pontos



## Liomar Oliveira (observações próprias)

- "Base WiFeed no fim do período:" A base é do ERP Voalle (base de clientes ativos ou adimplentes de toda a empresa), é bom atualizar este contexto. WiFeed é porque o relatório obtém todos os CPFs e CNPJs de todos os clientes adimplentes diariamente para atualizar os vouchers do WiFeed (sistema de captive Portal). Os textos tem que ter esse contexto.
- Vamos incluir uma nova seção, com os KPIs do Voalle, incluindo o dado acima reportado pelo relatório do WiFeed, que é da base ERP Voalle.
- Podemos reorganizar a ordem dos tópicos em grandes seções, como por exemplo:
    - O Setor de TI - Focar no operacional dos colaboradores analisados
      - Atividades extras e tópicos detectados de acordo com as atividades entrariam aqui, como por exemplo, o desafio, as conquistas, os fatos que impressionaram na semana...
    - A empresa - Dados que englobam a empresa como um todo, não só o Setor de TI. Exemplos: FullCam, WiFeed, Voalle ERP. Se os relatórios são oriundos do AutoTickets, por exemplo, este fato deve ser mencionado. Pois, como o AutoTickets é um grande integrador e centralizador de dados, ele irá reportar dados de sistemas, mas uqe foram gerados e consolidados por ele (e desenvolvido por mim, Liomar).
    - Sistemas - Assuntos que dizem respeito aos sistemas em si (AutoTickets e outros sistemas internos ou contratados da empresa), como desenvolvimento ou afins.

Estes tópicos serão aprimorados e repensados ao longo da semana.

- Checagens horárias da inadimplência FullCam sem registro desde 06/10: Na verdade, este relatório foi criado recentemente no AutoTickets. Lá, havia um log que eu implementei para acompanhar o funcionamento do agendador de tarefas do AutoTickets para esta automação (inadimplência) e também para a automação de instalações de câmera. O log registrava todas as ações realizadas pela automação que ela realiza de forma periódica, independente se houve ou não ações realizadas. Porém, para evitar excesso de informações inúteis, já removi este log (que foi criado apenas para feedback de desenvolvimento e confirmação da ferramenta) para que agora, passe a entrar no relatório apenas quando a automação atuou. Em casos que a automação executou e não fez nada, nenhuma informação será inserida no relatório. Portanto, não quer dizer que as automações não rodaram, apenas que ela não tomou nenhuma ação dentro do período analisado.
- A forma de escrever que está incomodando ao se referir às pessoas: "a Raimara, o David, o Liomar"... Normalmente, não falamos desta forma. Ao se referir à pessoas, pode ser reescrito desta forma, pra evitar estranhamento: "David atribui as falhas recorrentes", "Liomar registrou o estado dos sistemas ", "Raimara confirmou no equipamento", "Isac apurou 995 quedas e 29 dias, 11 horas de período a descontar"...

Todos os demais tópicos estão bem escritos e não precisam de alteração.
- "O #3217119 aparece com "Tempo de Atendimento" de 20.670 dias por erro de data no AutoTickets (pendência P1 #1), o que contamina o TMA do Liomar.". Feita correção no AutoTickets, os arquivos nos 4 formatos foram exportados novamente. Analise se foi corrigido e atualize no relatório semanal.

## Isac - Observações próprias

Sobre uma situação envolvendo instalação de câmera:
- Os links RTMP foram devidamente entregues no protocolo da instalação pela automação AutoTickets e estavam corretos. O erro reportado deve ser no contexto correto, que foi de digitação ou de colagem do link diretamente na configuração da câmera. O que foi detectado por Isac, após a equipe técnica (Davi Gabriel, configurado por Ailton) aciona-lo para informar que as câmeras não funcionaram, foi visto por Isac via acesso remoto que as duas câmeras estavam com o mesmo link (ocasionando queda em ambas) e ainda, os 2 links estavam com espaço e funcionou após Isac corrigir a configuração das câmeras via AnyDesk.
- Script Mikrotik: Contexto: O relatório está falando como se não houvesse um padrão de configuração no setor de TI . Realidade: Hoje já existe um padrão de configuração, com produção de scripts prontos e testados. O caso detectado foi de um cliente que teve seu Mikrotik configurado há 3 anos atrás (não existia Setor de TI e a configuração era realizada por terceiros, neste caso foi Emerson, hoje Supervisor de Suporte).
- Sobre o sistema Zeus sem movimentação durante a semana: O relatório fala bastante que faltaram relatos e ações durante a semana, mas na verdade, no último relato do protocolo já foi reportado que estávamos aguardando a chegada dos telefones para iniciarmos os testes da telefonia, o que ocorreu apenas no dia de ontem (situação que vai ser analisada nos dados da próxima semana).

## Respostas da equipe (opcional)

<!-- Respostas que Isac, David ou Liomar já deram ao Isvi; o novo relatório deve manter a coerência com elas. -->

- Nenhuma manifestação individual por parte dos demais colaboradores foi registrada / informada. 
