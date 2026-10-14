# 📁 2.1. Investigações Especiais, Segurança e Estudos de Infraestrutura (2.1.others)

Este diretório abriga estudos pontuais, investigações de vulnerabilidades, análises periciais e diagnósticos técnicos que vão além da rotina habitual de chamados do ERP Voalle.

---

## 📂 Organização por Data

Os estudos e relatórios técnicos são agrupados em subpastas datadas no padrão `YYYY-MM-DD`:

```text
2.1.others/
├── README.md                                    # Este documento de referência
└── [YYYY-MM-DD]/                                # Data de conclusão ou execução da investigação
    └── [tema_da_investigacao]/                  # Ex.: vulnerabilidades_sistemas_logistica
        ├── relatorio_investigacao_seguranca.md  # Relatório pericial detalhado
        ├── amostras_dados_e_auditoria_postman.md# Evidências e testes de API
        └── subdominios_ativos.json              # Mapeamento de superfície de ataque
```

---

## 🔍 Regra de Integração nos Relatórios Semanais

Quando houver uma pasta datada dentro do período da semana avaliado pelo `PROMPT.md`:

1. **Tópico 3 (Projetos e Entregas):** Registrar a condução do estudo de segurança como entrega técnica da semana.
2. **Tópico 7.3 (Atualizações, Melhorias e Segurança):** Resumir os testes executados e a superfície avaliada.
3. **Tópico 8.1 (Riscos Tecnológicos e Vulnerabilidades Identificadas):** Apresentar detalhadamente os riscos identificados, as falhas de controle e o plano de mitigação ou contenção recomendado.
