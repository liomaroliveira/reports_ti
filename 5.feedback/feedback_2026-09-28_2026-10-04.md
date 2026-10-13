# Feedback ao Relatório "report_ti-2026-09-28-2026-10-04.pdf":

# Isvi Neemias  [9h36]
Pessoal, bom dia!

Li com atenção o relatório do setor da semana passada e conferi os números com o Pontomais e com o relatório da semana anterior. Antes de tudo: a semana foi produtiva. Totem de Jacobina (+ PliQ) concluído, nobreak na Chácara, manutenção servidor, resposta rápida no caixa de Jacobina e na Cobrança, todos os itens de manutenção de informática e redes, muito apoio aos demais setores e um bom diagnóstico de apoio ao campo, evolução do AutoTickets, etc. Semana bem movimentada e com ótimo resultado. Obrigado pelo empenho.

# Isvi Neemias  [9h38]
Correções:

Item	No relatório	O que corrigir
Período	28/09 a 04/10	O padrão do relatório é domingo a sábado (27/09 a 03/10). Como o TI trabalha de segunda a sexta, o período efetivo é 28/09 a 02/10.
Resolutividade	108,6%	No Service Desk, resolutividade é outra métrica. Para ficar mais claro dentro da área Operacional, vamos utilizar "balanço da fila (saídas ÷ entradas)" ou “Backlog demandas” para esse indicador do setor de TI.
Lançamentos	84 lançamentos do setor e 84 apontamentos do David	O mesmo número aparece como total do setor e como total de uma pessoa. Verificar se está correto isso.
Horas do David	50h33 apontadas no Voalle	O Pontomais registrou 44h48 trabalhadas na semana. Explicar a diferença (tickets abertos por todo o período, deslocamento, sobreposição de atividades, solicitações em play quando fora de expediente (almoço, interjornada) etc.) ou corrigir.
Apoio ao campo	14 apoios com protocolo; tabela 6.2 soma 18; "~18 sem protocolo"	Todo apoio precisa de protocolo, verifica a abertura e execução sempre que possível. Quanto mais demandas formais (e registradas), melhor. Dúvidas e conversas rápidas são as exceções, mas se necessitou atuar de alguma forma, verificar algo, abrir alguma tela ou sistema, já vale a pena registar.
Acurácia pericial	100%, "sem reincidência"	Reincidência seria interessante adotar 30 dias de observação.
Índice	Seções 5.1 e 6.1	Constam no índice e não aparecem no relatório.

# Isvi Neemias  [9h40]
Perguntas:

1. SIEM Wazuh e VPN: na semana anterior, o túnel estava validado em Quixabeira e Campo Formoso, com script pronto para as 28 filiais, previsão para 02/10 e início em 5 filiais. Este relatório fala só da sede (RB TI e RB Chácara). Qual o status das filiais, o percentual e o novo prazo?.
2. Compras da semana anterior: a tela do notebook (#3202572) agora consta como destino "Estoque/TI"; antes era o notebook de campo do Felipe Nere. Qual o status das 10 câmeras? Alguma dificuldade em relação a compras?.
3. Deslocamentos: Como está sendo o uso de veículos? alguma dificuldade ou atraso gerado pela frota?.
4. Disponibilidade: de onde vêm os 99,8% do Voalle? e 100% de disponibilidade de outros serviços?.
5. Backup: Os backups foram validados como (quantas VMs, já houve teste de restauração)?.

## Isac Costa:
4. O gap de porcentagem do Voalle foi devido a falha de sessão que Liomar relatou no protocolo 3209683. Não necessariamente é uma indisponibilidade, mas é uma ocorrência do sistema. Os 100% dos outros serviços vêm da ausência de erros nos servidores correspondentes, vamos tentar detalhar mais na próxima.

5. As rotinas de backups dos servidores estão todas ok, já foi validado que todas as vms e cts estão dentro das rotinas diárias. Os backups manuais que eu realizei são das vms que falharam por algum motivo (geralmente uma queda de conexão no momento do backup), quando é realizado eu adiciono as informações da VM.

## David Brasil:
1- Decidi refazer o túnel e focar na RB que mais teve acessos indevidos.
Então foquei na do TI e da Chácará, para a pois o período de testes expandir para as outras localidades.
2-A tela está sendo aguardada chegar aqui no setor, do notebook que felipe nere entregou dos técnicos.
2.1-Sobre as câmeras está aguardando a confirmação do compras. Protocolo ja foi enviado para eles e passado todas as informações.
3- Sobre os carros, mesmo com o protocolo aberto com antecedência , quando chega para retirar sempre vem a resposta " Vou verificar qual carro posso disponibilizar"

## Isvi Neemias:
Dois ajustes para o próximo relatório:

Disponibilidade: se a falha de sessão do Voalle não é indisponibilidade, ela não deve virar percentual, para não ter dados mensurados de forma não factual e não replicável (eu posso dizer que impactou 1%, por exemplo, é o meu "achismo"). 100% por ausência de erros não é uma medição de tempo no ar.

Proposta:

• Se tivermos monitoramento (não lembro se a página de monitoramento ainda funcionado, depois que subiu pra Cloud, onde monitorava o uso da VM) que meça o tempo de atividade, informar o % com a fonte e o tempo fora do ar..
• Se não tivermos, usar "sem indisponibilidade registrada" e listar à parte as ocorrências, como a sessão do Voalle (#3209683). Pode citar impacto e danos causados ou previstos, mas como "ocorrências".

Backups: bom saber que todas as VMs estão na rotina diária e que as falhas são refeitas. Só que isso confirma que o backup rodou, não que ele restaura.

Para o relatório, sugiro trazer:

• quantas VMs e CTs estão na rotina.
• quantos jobs rodaram e quantos falharam na semana.
• quais foram refeitos manualmente.
• a data do último teste de restauração.

Bom definir uma rotina de teste de restauração, por exemplo uma VM ou duas por mês em rodízio. Pode estruturar esse processo e começar fazer verificação, mas em caráter secundário, gostaria de manter o foco maior na questão do serviço de telefonia fixa, para evoluirmos o quanto antes essa parte.

## Isvi Neemias:
Wazuh e VPN:
Faz sentido priorizar a RB com mais acessos indevidos. Só que isso muda o plano que estava no relatório anterior (túnel validado em Quixabeira e Campo Formoso, script pronto e início em 5 filiais). Não tem problema, mas é importante atualizar os detalhes, ainda que sejam mudanças de curso, no relatório, para ficar tudo bem amarrado. Mudança de escopo ou de prioridade entra no relatório com o motivo.

Compras:

Tela do notebook: ok
Câmeras: vou falar com Daniel pra ver se consegue agilizar isso.


Veículos:
Entendi a questão. Como você é quem mais utiliza veículos, tenta gerar um report semanal enviado diretamente pra mim sobre essas questões, em detalhes: Data, protocolo da requisição, horário combinado × horário em que recebeu o carro e o que foi afetado (visita adiada, tempo perdido). Pode ser uma lista simples, não carece um relatório elaborado como o semana.

Obg (editado)

# Isvi Neemias  [9h44]
Outros Pontos:

Windows 10: foi instalado em Sisalândia e no PC da Cobrança. O suporte da Microsoft ao Windows 10 terminou em outubro de 2025. Importante definirmos o padrão para novas instalações, como adotar o uso do Windows 11 (ou motivos para não fazê-lo). Verificar como está a gestão de licenças do Windows e informar a situação no próximo relatório semanal.
AutoTickets (e talvez outros projetos): Caso deseje, posso gerar uma chave LLM na OpenAI para uso na plataforma, utilizando os recursos que temos disponíveis nessa área.
Slack × AutoTickets (#3210508): a integração para contornar o limite de 90 dias do plano gratuito envolve retenção de dados pessoais (LGPD) e as regras de uso do Slack. Precisamos realizar alinhamento antes disso entrar em produção para todos os colaboradores do Workspace.
ChatSeguro: cancelamento solicitado em 30/09, com aviso de 30 dias
BI Analítica 3M: Alterei o perfil de Liomar para master. Com isso, ele pode gerir usuários. O BI possibilita ter acesso a informações críticas da operação, por isso, peço que mantenha o acesso apenas consigo, no momento. Caso alguma tela já existente seja de interesse ou útil para o setor, pode criar um perfil (grupo) e gerar usuário para David e Isac, com acesso a essas telas.
Easy BI: também tenho acesso limitado, uma única tela que pouca agrega. Pra ser direto, acreditoq eu o Easy BI está longe de ser um substituto do Analítica 3M, que está muito mais maduro e personalizado para nossa operação, provavelmente, não vamos manter esse módulo no pacote da MW Solutions.

# Isvi Neemias  [9h47]
Agradeço a todos pelas contribuições para o relatório, é apenas a terceira semana e já temos algo muito positivo sendo construído. :clap:

# Liomar Oliveira  [9h48]
Também agradeço pelo feedback. Vi aí pontos muito interessantes pra considerarmos. Vamos passar a semana inteira se debruçando sobre seus apontamentos e gerar novas demandas.

# Liomar Oliveira  [9h49]
Sobre o relatório, ainda não me sinto confortável, pois ainda não está da forma como eu gostaria. Estou aprimorando a coleta e organização dos dados com ajuda do AutoTickets pra tentar ser o mais determinístico possível e evitar erros de semântica e colocar no nosso contexto ao máximo. Confesso que não é fácil e que vai levar um tempo até ficar 100% confiável, mas estou otimista com o progresso e com as ideias que estão saindo desta geração de relatório.

## Isvi Neemias  [9h53]
Com certeza, é natural que leve um tempo até estar beirando a perfeição, é uma evolução constante, mas precisamos reconhecer o caminho até aqui, já foram grandes passos, saindo do zero para um resultado muito bom, é agradável visualmente (muito parecido em alguns pontos com o que eu gerava, até adotei algumas características pra o meu modelo hehe), traz informações úteis, segue um raciocínio claro de gestão de indicadores, de atividades, de tempo, de resultado, consegue cumprir bem o propósito de um relatório.

## Liomar Oliveira  [9h53]
Que bom!
[9h54]Bora pra cima!
## Isvi Neemias  [9h57]
Curiosamente, semana passada tive uma conversa sobre o relatório de outra equipe, estava ocorrendo alguns problemas com a intenção e propósitos de um relatório. Eu estava crente que é algo subentendido, mas de senso comum a todos, e percebi que não é. Naquele momento, tinha um líder em dúvida de como apresentar o relatório em relação às expectativas que temos sobre ele. Confirmei aquele velho ditado: O óbvio precisa ser dito.

# Liomar Oliveira  [9h50]
Peço um pouco de paciência, mas tenho certeza que em breve, termos dados mais maduros e totalmente localizados com nosso contexto.
[9h50]Eu e os demais vamos ficar respondendo dentro dos seus apontamentos sobre cada resposta que tivermos.
[9h51]Vamos criar outro relatório em cima desses apontamentos e gerar as nova demandas (ou atualizar as atuais). Se for algo muito importante, informaremos aqui sob demanda. Caso não, aparecerá no próximo relatório.

# Isvi Neemias  [9h57]
respondeu em uma conversa:Curiosamente, semana passada tive uma conversa sobre o relatório de outra equipe, estava ocorrendo alguns problemas com a intenção e propósitos de um relatório. Eu estava crente que é algo subentendido, mas de senso comum a todos, e percebi que não é. Naquele momento, tinha um líder em dúvida de como apresentar o relatório em relação às expectativas que temos sobre ele. Confirmei aquele velho ditado: O óbvio precisa ser dito.
[9h57]Vou mandar aqui o que respondi sobre propósito para mantermos isso alinhado e claro:

[9h58]
- Registrar fatos: documentar o que aconteceu, quando, onde e com quais envolvidos.
- Apresentar resultados: mostrar indicadores, metas, entregas e desempenho.
- Analisar uma situação: identificar causas, tendências, problemas e impactos.
- Dar visibilidade: permitir que gestores e outras áreas entendam o que está acontecendo sem precisar acompanhar toda a operação.
- Apoiar decisões: fornecer evidências para decidir o que fazer a seguir.
Acompanhar evolução: comparar períodos, metas e resultados.
- Criar histórico: manter uma referência para consultas futuras e prestação de contas.
- Recomendar ações: quando apropriado, indicar próximos passos com base na análise.

[10h]É isso que tenho mentalmente enraizado sobre o porquê relatórios são importantes. Se cumprirmos isso, o relatório faz sentido, se torna útil, uma ferramenta para ações, para o futuro, deixa de ser apenas registro "do que fizemos" e começa a falar sobre "foi bom?", "para onde estamos apontando?", "o que precisa mudar?", "que tipo de profissionais somos? (como um time e individualmente tbm)".
[10h01]E vejo que estamos seguindo bem essa linha de raciocínio aqui, vamos amadurecer mais e mais

# Liomar Oliveira  [10h03]
Concordo totalmente.

------

