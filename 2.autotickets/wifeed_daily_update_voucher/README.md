# Sobre
Neste relatório, contém os dados de atualização de voucher do AutoTickets na plataforma WiFeed. Explicando a integração:

# Contexto Geral
- O WiFeed é um sistema de Captive Portal, no qual o provedor de internet que trabalho utiliza para configurar Hotspots em locais estratégicos em cidades de atuação, principalmente para captura de leads, divulgação de promoções, campanhas e outros e, como uma extensão do seu produto conexão com a internet, de forma a fornecer conectividade fora da residência ou empresa do cliente nestes locais estratégicos e em estabelecimentos credenciados. 

Como funciona: 
- O cliente ou não cliente enxergará a rede "TEN_Wi-Fi" em seus dispositivos wireless. A rede é aberta em formato Captive Portal. A conexão fornecida é em média, 5 a 15 MB Download e 3 a 5 MB Upload, com renovação de 1h a 2h para não clientes e 4 a 12 horas para clientes.
- Haverá duas formas de liberação de conexão com à internet:
    1. Não Sou Cliente: Caso o usuário nunca tenha utilizado o hotspot, deverá preencher um pequeno cadastro com Nome, Cidade e número de celular. Nas próximas vezes que for utilizar, não importa a cidade ou ponto de acesso, os dados deste usuário permanecerão e basta informar apenas o celular que a conexão liberará automaticamente, sem a necessidade de novos preenchimentos.
    2. Sou Cliente - Informar CPF: O usuário deverá fornecer um número de CPF, desde que seja do titular do contrato de serviço contratado com o provedor. Ao validar este CPF com a base de dados de vouchers interna do WiFeed, o sistema libera a autenticação como cliente. O mecanismo interno para esta funcionalidade chama-se voucher. 
- 

# Problema
O voucher do WiFeed é um arquivo CSV de coluna única, contendo os CPFs ou CNPJs já sanitizados sem pontos ou traços, que deve ser feito upload manualmente para ser utilizado como forma de autenticar nos hotspots. 

Ou seja, a atualização dos vouchers na plataforma e o tratamento da formatação dos dados internos do csv é 100% manual.

Além disso, se os vouchers não forem atualizados, pode gerar sensação de "propaganda enganosa" para a empresa, ao vender que o cliente pode utilizar o hotspot como pontos de acesso extenso, e ao tentar utilizar com seu CPF, se deparar com erros de não autorizado, pois a última atualização manual foi feita antes da assinatura que o cliente fez.

E por fim, o tempo perdido com tarefas manuais e repetitivas, onde o colaborador do Setor de TI poderia estar dedicando para outras tarefas mais importantes e complexas.

# Solução implementada
Desenvolvi uma automação em AutoTickets que faz o seguinte:
- Conecta no banco de dados Voalle;
- Valida apenas os clientes que estão com contratos adimplentes em quaisquer produtos e serviços contratados;
- Cria uma lista apenas com seus CPFs e CNPJs e sanitiza-os, deixando apenas os números
- Lança a quantidade total de clientes como "Clientes Ativos no ERP" para geração de gráfico e cálculo de variação diária, semanal e crescimento acumulado no AutoTickets;
- Um endpoint específico para exportação do arquivo CSV já pronto para upload na plataforma;
- Um job automático que já gera o csv e faz o trabalho "sujo" dentro da plataforma WiFeed em passos sequenciais:
    - Em horário agendado diariamente (11h da manhã), o AutoTickets executa a automação que navega para os endpoints de segmentos de voucher (com as bases de dados dos clientes em csv), remove o segmento atualmente utilizado, cria um novo segmento, faz o upload e lança uma paginação em um endpoint específico para contar se todas as linhas do csv foram salvas no sistema WiFeed. Após validar que os dados estão íntegros, o sistema efetua a troca do segmento padrão para o novo segmento criado, totalmente atualizado.
