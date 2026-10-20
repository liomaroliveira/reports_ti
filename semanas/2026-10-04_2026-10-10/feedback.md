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

- Sobre o relatório do FullCam. Consta registro de David (Brasil Fernandes): o contrato dele aparece com faturamento de videomonitoramento, mas tem faturas de R$ 10/mês que não parecem de câmera e o contrato não tem etiqueta do serviço. Verifiquem se a regra do módulo está pegando contratos sem câmera ou o que pode significar. 
  - Liomar Oliveira: Sobre isso, para os próximos relatórios, ignorar totalmente a informação vinda de DAVID BRASIL FERNANDES neste relatório (semanas/2026-10-11_2026-10-17/fontes/autotickets/fullcam_lucros_prejuizos), trata-se de um equívoco no sistema, que será entendido porque o dado está sendo obtido pelo relatório e corrigido posteriormente.
- Aproveitar o exemplo de Liomar: 274h17 apontadas pelo play na solicitação deixados abertos, acredito ter também sobreposição de atividades, o que já é esperado. Vamos combinar o fechamento do(s) relato(s) no fim do expediente, para os apontamentos refletir a jornada o mais fiel possível ao que ocorreu. Além disso, pausar sempre que estiver com foco real em outra atividade, mitigar essas sobreposições de atividades quando possível.

### Perguntas

- Sem perguntas realizadas.

### Orientações e outros pontos

- Sobre a questão da frota: dessa vez, reportei diretamente Edriano a dificuldade de retirada de veículos, mesmo com requisição antecipada. Como Frota está em Suprimentos e Logística, ele vai verificar os trâmites com a gestão, já havia tentado de forma pessoal mas percebo que persiste. Continuem registrando cada ocorrência com horário combinado e liberado, além de reportar impacto.
  - Liomar Oliveira: Edriano Conceição é o Diretor Operacional da Empresa, COO.
- Histórico do Slack: vamos deixar uma reunião de acompanhamento de escopo no fim do mês. Mas, para agilizar estudo e desenvolvimento, Liomar pode adiantar a aplicação já pensando no armazenamento seguro: arquivo criptografado, retenção por tempo indeterminado e acesso só por MFA 'simultâneo' de 3 entre 6 responsáveis (no momento, planejei: TI, Isvi, Edriano COO, Saulo CEO, RH e DP como partes interessadas que podem gerar a autenticação em 3 vias/tokens). Dessa forma, o acesso aos dados armazenados ficam restritos a ter sempre 3 frentes autorizantes para acessar as informações.
  - Liomar Oliveira: Adicionar como pendência para ser vista nos próximos relatórios, com marca de frase de atenção em tópico apropriado.
- Descrição de cargos: Liomar abriu o protocolo 3218356 pedindo ao RH os documentos institucionais (código de conduta, regulamento, plano de cargos, organograma, benefícios, políticas), que são de responsabilidade do RH e do DP. Eu atuo só na descrição dos cargos do setor de Tecnologia, que estou refazendo para validar com o RH até o fim de novembro (pedi ao RH para dar esse retorno com o prazo). O documento que me enviaram estava parcialmente preenchido, com a maioria dos cargos com informações vazias, acredito que templates minimamente preenchidos. Comecei trabalhar nisso, assim que possível, marco o RH reunião de validação dos dados.
- Por fim, tenho uma ideia bacana, é uma tarefa/demanda para o setor, quase que uma gincana ou desafio, podendo ser realizado individualmente ou em grupo, como preferirem (após decidir, abrir protocolos para registar a demanda):
  - Testes de vulnerabilidade (segurança) nos nossos sistemas próprios
  - Cada um pode usar até 9h (limite, não necessita utilizar todo esse tempo) de expediente na próxima semana para explorar falhas, começando pelo sistema de Compras (compras.teninternet.com.br, de Daniel, o mesmo do incidente de sexta-feira passada).
  - Entreguem relatório (à parte do semanal, o semanal pode conter a descrição da tarefa e o resumo) contendo as falhas encontradas, o nível de risco, as correções e as melhorias sugeridas. Depois seguimos para os demais sistemas internos (os meus, outro de Daniel e o Ciclos que foi feito por Edriano) e, mais adiante, os de terceiros (Voalle, PliQ, Fortics, Power BIs, etc). Vou passando um sistema por vez, conforme finalizado o pentest da rodada.

## Liomar Oliveira (observações próprias)

- Já estou tomando ações para não deixar protocolos em play após o expediente sem de fato estar trabalhando neles.
- Destacar a continuidade na tratativa do protocolo que fala sobre o incidente de credenciais e vulnerabilidade exposta no sistema de Compras da empresa, com o desdobramento de Isvi sobre a "Gincana" ou "Desafio" proposto. Nosso time de TI (Liomar, Isac e David) irá se preparar para executar a ação ainda nesta semana, onde serão abertos protocolos específicos para registrar a tratativa e produzido relatório individual na próxima semana junto do relatório semanal.

## Respostas da equipe (opcional)

<!-- Respostas que Isac, David ou Liomar já deram ao Isvi; o novo relatório deve manter a coerência com elas. -->

- Nenhuma manifestação individual por parte dos demais colaboradores foi registrada / informada. 
