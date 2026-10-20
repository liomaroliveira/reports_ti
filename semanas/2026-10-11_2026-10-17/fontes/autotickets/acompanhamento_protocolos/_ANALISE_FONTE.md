# Análise da fonte: Acompanhamento de protocolos (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos:** `analise-lista-de-26-protocolos-2.md` e `analise-lista-de-26-protocolos-2.pdf`

## O que é

É uma análise **gerada por IA local** sobre 26 protocolos que o TI abriu para outros setores entre 26/03/2026 11:50 e 19/10/2026 07:20. Os protocolos tratam de estoque, compras, manutenção, câmeras offline em POPs, notebooks, ar-condicionado do DC-Chácara e nobreaks NHS.

- **Período:** é uma lista acumulada de protocolos abertos, não um recorte da semana.
- **Data de geração inconsistente:** o arquivo diz "Gerado em: 19/10/2026 10:00", mas o PDF foi criado às 21:57:41. O sufixo `-2` sugere que foi o segundo download.
- **MD e PDF são idênticos:** os dois têm 26 protocolos, 64 relatos, 9 eventos de linha do tempo, 4 resolvidos, 20 pendências e 20 próximos passos.

## Inconsistências

- **Status contraditório:** os 26 aparecem como "Novo" e "Encerrado N/D". Mesmo assim, a seção "Resolvidos" lista 4: 3192572, 3183222, 3195768 e 3225109.
- **3306821:** a numeração está fora da sequência (aberto em 09/06, mas com número maior que 3225109). Pode ser erro de digitação ou **alucinação da IA**. É preciso conferir no Voalle.
- **3222238:** aparece no `colaborador_x_ticket` como Concluído em 19/10 16:38, depois da geração desta análise. Também está classificado em duas categorias.
- **Protocolos sem classificação:** 3306821 e 3145634 não estão nem em pendências nem em resolvidos.
- **Seções repetidas:** "Próximos passos" repete as pendências quase literalmente e cita o protocolo duas vezes. Exemplo: "no protocolo 3024008. (protocolo 3024008)".
- **Percepção do cliente inferida:** a seção foi preenchida pela IA, com satisfação N/D.

## Dados sensíveis

Nenhum CPF, CNPJ, telefone ou e-mail. Aparecem apenas nomes de colaboradores.

## Como usar no relatório (com cautela)

- **1.1 Demandas Pendentes:** idade do backlog (a mais antiga é de março).
- **9.2 Investimentos:** nobreaks NHS, notebook e cordões ópticos.
- **8.3 / Fatos Notáveis:** ar-condicionado do DC-Chácara em 14/10 e câmeras offline em POPs.
- **Pergunta do Isvi sobre compras e câmeras** (feedback da semana 40).

Para todos esses usos, **filtre os eventos de 11/10 a 17/10 e confirme status e datas no Voalle**. É texto não determinístico.

## Formato recomendado

**MD.** O PDF não acrescenta nada.

## Correções sugeridas ao AutoTickets (por prioridade)

1. **Exportar também a tabela determinística (CSV)** com protocolo, setor de destino, situação real no Voalle, data de abertura, data do último relato e responsável. A análise da IA fica como complemento.
2. **Validar os protocolos citados pela IA** contra a lista de entrada, para evitar números inexistentes como o 3306821.
3. **Usar o status real** do Voalle em vez de "Novo" fixo.
4. **Atualizar a data de geração** no momento da exportação.
5. **Remover ou fundir a seção "Próximos passos"**, que é redundante com as pendências.
