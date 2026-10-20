#!/usr/bin/env python3
"""
Mascara dados sensíveis (LGPD e credenciais) em arquivos de texto antes de versionar exportações brutas.

O que é mascarado:
  - CPF formatado ou só dígitos (com dígito verificador válido)  -> ***.BBB.CCC-**
  - CNPJ formatado ou só dígitos (com dígito verificador válido) -> **.BBB.CCC/****-**
  - Em CSV, qualquer valor das colunas cujo cabeçalho contém "CPF" ou "CNPJ" (mesmo com DV inválido)
  - URLs RTMP/RTMPS (stream key de câmeras)                    -> rtmp://host/***
  - E-mails fora do domínio da empresa                           -> a***@dominio
  - Senhas em texto ("Senha: xxx", "Senha- xxx", "Password = xxx")             -> Senha: ********

Uso:
    python3 scripts/mascarar_dados.py semanas/<semana>/fontes/voalle/* semanas/<semana>/fontes/autotickets/*/*
    python3 scripts/mascarar_dados.py --check <arquivos>     # só verifica (sai com 1 se encontrar algo)
    git show :arquivo | python3 scripts/mascarar_dados.py --check -    # verifica a entrada padrão

PDFs não são alterados: para PDFs, gere a partir do HTML/CSV já mascarado.
"""

import csv
import io
import re
import sys

TEXT_EXT = (".md", ".html", ".htm", ".csv", ".txt", ".json")
DOMINIOS_INTERNOS = ("teninternet.com.br", "teninternet.net")

CPF_FMT = re.compile(r"\b\d{3}\.(\d{3})\.(\d{3})-\d{2}\b")
CNPJ_FMT = re.compile(r"\b\d{2}\.(\d{3})\.(\d{3})/\d{4}-\d{2}\b")
DIGITOS = re.compile(r"(?<![\d.,/-])(\d{11}|\d{14})(?![\d,]|\.\d)")
RTMP = re.compile(r"\b(rtmps?://[^/\s\"'<>;]+)/[^\s\"'<>;]+", re.I)
EMAIL = re.compile(r"\b([A-Za-z0-9])[A-Za-z0-9._%+-]*@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
SENHA = re.compile(r"(?i)(senha|password|passwd|pwd)(\s*(?:[:=]|-(?=\s))\s*)(?!\*{8})([^\s<\"';,]+)")


def cpf_valido(d):
    if len(d) != 11 or d == d[0] * 11:
        return False
    for n in (9, 10):
        s = sum(int(d[i]) * (n + 1 - i) for i in range(n))
        if (s * 10 % 11) % 10 != int(d[n]):
            return False
    return True


def cnpj_valido(d):
    if len(d) != 14 or d == d[0] * 14:
        return False
    for n, pesos in ((12, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]), (13, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])):
        r = sum(int(d[i]) * pesos[i] for i in range(n)) % 11
        if (0 if r < 2 else 11 - r) != int(d[n]):
            return False
    return True


def mascara_documento(d):
    d = re.sub(r"\D", "", d)
    if len(d) == 11:
        return f"***.{d[3:6]}.{d[6:9]}-**"
    if len(d) == 14:
        return f"**.{d[2:5]}.{d[5:8]}/****-**"
    return "***" if d else ""


def _digitos(m):
    d = m.group(1)
    if (len(d) == 11 and cpf_valido(d)) or (len(d) == 14 and cnpj_valido(d)):
        return mascara_documento(d)
    return d


def _email(m):
    if any(d in m.group(2).lower() for d in DOMINIOS_INTERNOS):
        return m.group(0)
    return f"{m.group(1)}***@{m.group(2)}"


def _documentos_csv(texto):
    """Valores das colunas CPF/CNPJ de um CSV (mascarados mesmo com DV inválido)."""
    amostra = texto.lstrip("﻿")[:4096]
    try:
        dialeto = csv.Sniffer().sniff(amostra, delimiters=";,\t")
    except csv.Error:
        return set()
    linhas = csv.reader(io.StringIO(texto.lstrip("﻿")), dialeto)
    cab = next(linhas, [])
    cols = [i for i, c in enumerate(cab) if re.search(r"cpf|cnpj", c, re.I)]
    valores = set()
    for linha in linhas:
        for i in cols:
            if i < len(linha) and re.search(r"\d{5,}", linha[i]):
                valores.add(linha[i].strip())
    return valores


def mascarar(texto, csv_mode=False):
    """Retorna (texto_mascarado, quantidade_de_substituições)."""
    total = 0
    if csv_mode:
        for v in sorted(_documentos_csv(texto), key=len, reverse=True):
            texto, n = re.subn(r"(?<![\d*])" + re.escape(v) + r"(?!\d)", mascara_documento(v), texto)
            total += n
    for padrao, repl in (
        (CPF_FMT, lambda m: f"***.{m.group(1)}.{m.group(2)}-**"),
        (CNPJ_FMT, lambda m: f"**.{m.group(1)}.{m.group(2)}/****-**"),
        (DIGITOS, _digitos),
        (RTMP, lambda m: f"{m.group(1)}/***"),
        (EMAIL, _email),
        (SENHA, lambda m: f"{m.group(1)}{m.group(2)}********"),
    ):
        def contar(m, repl=repl):
            nonlocal total
            r = repl(m)
            total += r != m.group(0)
            return r
        texto = padrao.sub(contar, texto)
    return texto, total


def pendencias(texto, csv_mode=False):
    """Quantidade de dados sensíveis ainda sem máscara (usado por checar_entradas.py e pelo pre-commit)."""
    return mascarar(texto, csv_mode)[1]


def main(args):
    check = "--check" in args
    paths = [a for a in args if a != "--check"]
    if not paths:
        print(__doc__)
        return 1
    total = 0
    for path in paths:
        if path == "-":
            texto = sys.stdin.read()
            n = pendencias(texto, csv_mode=texto.lstrip("﻿")[:2048].count(";") > 3)
            total += n
            print(f"[{'PENDENTE' if n else 'OK'}] <stdin>: {n} dado(s) sensível(is)")
            continue
        if not path.lower().endswith(TEXT_EXT):
            if not check:
                print(f"[IGNORADO] {path} (não é texto; gere o PDF a partir da versão mascarada)")
            continue
        with open(path, "r", encoding="utf-8", errors="surrogateescape", newline="") as f:
            original = f.read()
        novo, n = mascarar(original, csv_mode=path.lower().endswith(".csv"))
        total += n
        if check:
            if n:
                print(f"[PENDENTE] {path}: {n} dado(s) sensível(is) sem máscara")
            continue
        if n:
            with open(path, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                f.write(novo)
        print(f"[OK] {path}: {n} item(ns) mascarado(s)")
    print(f"Total: {total}")
    return 1 if (check and total) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
