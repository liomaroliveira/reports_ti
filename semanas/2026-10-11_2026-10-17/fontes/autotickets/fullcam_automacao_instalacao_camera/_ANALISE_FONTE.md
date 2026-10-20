# Análise da fonte — Fullcam: automação de instalação de câmeras (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos:**
- `relatorio_fullcam_installations_2026_10_19_220221.md`
- `…_220224.csv`
- `…_220228.html`
- `Instalações de Câmeras - AutoTickets.pdf`

## Período

- **Janela declarada:** todos os formatos dizem **20/09/2026 a 20/10/2026**. Na semana 41 a janela era 01/10 a 14/10, então ela mudou de uma semana para outra e se sobrepõe à anterior.
- **Registro depois da semana:** o #846 é de **19/10**, depois do fim da semana.

## Contagens por formato

- **Total:** 216 registros em todos os formatos. O PDF tem 22 páginas.
- **Ações de instalação:** 7 INSTALL/success, sendo **5 na semana**: #786 (15/10), #798, #799, #802 e #807 (16/10).
- **Avisos:** 209 NOTIFY/warning (97%).

| Diferença | Onde |
| :--- | :--- |
| Mensagem ausente | MD |
| Mensagem truncada com "…" (215 ocorrências) | HTML e PDF |
| Mensagem completa | CSV |
| "Cliente N/D" na coluna, com o nome dentro da mensagem | NOTIFY, em todos os formatos |
| Mensagem de etapa ("Etapa 3/3") no lugar do texto padrão | #746 |

## Inconsistências de dados

- **Avisos idênticos:** os 209 avisos são **iguais entre si**. Todos se referem ao protocolo **3198228**, contrato interno 85854, com a mensagem "Nenhuma câmera localizada no FullCam", repetida a cada 2 h de 20/09 a 08/10. É um item preso na fila: **vale tratar o protocolo 3198228 (fechar ou corrigir o cadastro)**.
- **KPIs que contam aviso como falha:** "Ações com Sucesso 7/216" e "Sucesso 3,2%" tratam avisos como falha e dão a impressão de uma esteira com 97% de falha.
- **Contagem de câmeras errada:** "Câmeras Afetadas 7" não confere. O #786 tem "Câmeras = 1", mas a mensagem lista **3 câmeras**, então o total real é 9.

## Dados sensíveis (já mascarados no CSV desta pasta)

- O **CSV** tinha **6 e-mails de clientes** e **8 URLs RTMP com stream key**, que funcionam como credencial de acesso à câmera. Foram mascarados em 19/10 com `scripts/mascarar_dados.py`.
- MD, HTML e PDF não expõem esses dados, porque truncam ou omitem a mensagem.

## Formato recomendado

O **MD**, depois de descartar os 209 avisos repetidos. O CSV só deve ser usado já mascarado.

## Correções sugeridas ao AutoTickets (por prioridade)

1. **Mascarar as URLs RTMP (stream key) e os e-mails na origem.** É urgente: a stream key permite assistir à câmera do cliente.
2. **Agrupar avisos repetidos**, por exemplo: "protocolo 3198228 pendente desde 20/09, N tentativas, última em DD/MM".
3. **Calcular as câmeras a partir da lista real** contida na mensagem.
4. **Separar sucesso, aviso e erro** nos KPIs, para que aviso não conte como falha.
5. **Recortar pelo período solicitado.**
