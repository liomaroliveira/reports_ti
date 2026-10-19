#!/usr/bin/env python3
"""
Utilitário de consulta do histórico de WhatsApp para os relatórios semanais do Setor de TI.
Permite selecionar mensagens por intervalo temporal e categoria de operação:
- campo: Suporte a técnicos de campo (ServiceDesk, Projetos TEN, Ativações)
- interno: Suporte interno a computadores, acessos e setores da empresa
- coordenacao: Alinhamentos com a Coordenação de TI (Isvi Neemias)
- incidentes: Tratativas de incidentes com Made4NOC e parceiros
- all: Todas as conversas ativas no período
"""

import os
import re
import sys
import json
import sqlite3
import argparse
from datetime import datetime, time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "msgstore.db")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")

os.makedirs(EXPORTS_DIR, exist_ok=True)

# Mapeamento de contatos conhecidos (telefone -> nome), mantido fora do Git
CONTACTS_FILE = os.path.join(BASE_DIR, "contatos_conhecidos.json")
KNOWN_CONTACTS = {}
if os.path.isfile(CONTACTS_FILE):
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        KNOWN_CONTACTS = json.load(f)

# Categorização de canais
CATEGORY_RULES = {
    "campo": [
        "servicedesk suporte ao técnico",
        "projetos ten - apoio ao técnico",
        "ativações rede megas",
        "equipe volante",
        "apoio ao técnico",
        "suporte ourolândia",
        "serrolândia",
        "santaluz",
        "jacobina",
        "técnico",
        "equipe"
    ],
    "interno": [
        "tecnologia ten",
        "suporte e ti - ten",
        "manutenção de computadores",
        "all inclusive - ten",
        "marketing",
        "cobrança",
        "financeiro",
        "estoque",
        "frota",
        "comercial"
    ],
    "coordenacao": [
        "isvi"
    ],
    "incidentes": [
        "made4noc",
        "consultoria",
        "pliqcx"
    ]
}

def load_database():
    if not os.path.isfile(DB_PATH):
        print(f"[ERRO] Banco de dados não encontrado em: {DB_PATH}")
        print("Execute primeiro: python 3.whatsapp_histories/scripts/sync_backup.py")
        sys.exit(1)
    return sqlite3.connect(DB_PATH)

def get_sender_resolver(conn):
    c = conn.cursor()
    jid_rows = c.execute("SELECT _id, user, server, raw_string FROM jid").fetchall()
    jids = {r[0]: {"user": r[1], "server": r[2], "raw": r[3]} for r in jid_rows}
    
    lid_map = {}
    for r in c.execute("SELECT lid_row_id, jid_row_id FROM jid_map").fetchall():
        lid_map[r[0]] = r[1]
    
    def resolve_name(jid_id, is_from_me=False):
        if is_from_me:
            return "Você (Liomar TI)"
        if not jid_id or jid_id not in jids:
            return "Desconhecido"
        if jid_id in lid_map:
            jid_id = lid_map[jid_id]
        info = jids.get(jid_id, {})
        user = info.get("user", "")
        if user in KNOWN_CONTACTS:
            return KNOWN_CONTACTS[user]
        for k, v in KNOWN_CONTACTS.items():
            if user and len(user) >= 8 and len(k) >= 8 and user[-8:] == k[-8:]:
                return v
        return user if user else info.get("raw", "Desconhecido")
    
    return resolve_name

def classify_chat(subject, raw_jid):
    sub = (subject or "").lower()
    raw = (raw_jid or "").lower()
    
    coord_numbers = [num for num, nome in KNOWN_CONTACTS.items() if "coordena" in nome.lower()]
    if any(num in raw for num in coord_numbers) or "isvi" in sub:
        return "coordenacao"
    if any(k in sub for k in ["made4noc", "consultoria", "pliqcx"]):
        return "incidentes"
    if any(k in sub for k in ["servicedesk", "projetos ten", "ativações", "técnico", "volante", "suporte"]):
        return "campo"
    if any(k in sub for k in ["tecnologia ten", "manutenção de computadores", "marketing", "cobrança", "financeiro", "estoque", "frota"]):
        return "interno"
    return "outros"

def query_messages(conn, start_dt, end_dt, category=None):
    start_ts = int(start_dt.timestamp() * 1000)
    end_ts = int(end_dt.timestamp() * 1000)
    
    c = conn.cursor()
    resolve_sender = get_sender_resolver(conn)
    
    # Busca conversas com mensagens no período
    query = """
        SELECT m._id, m.chat_row_id, c.subject, j.raw_string, m.timestamp, m.from_me, 
               m.sender_jid_row_id, m.text_data, m.message_type
        FROM message m
        JOIN chat c ON m.chat_row_id = c._id
        JOIN jid j ON c.jid_row_id = j._id
        WHERE m.timestamp >= ? AND m.timestamp <= ?
        ORDER BY c._id, m.timestamp ASC
    """
    rows = c.execute(query, (start_ts, end_ts)).fetchall()
    
    results_by_cat = {
        "campo": {},
        "interno": {},
        "coordenacao": {},
        "incidentes": {},
        "outros": {}
    }
    
    total_msgs = 0
    
    for row in rows:
        msg_id, chat_id, subject, raw_jid, ts, from_me, sender_id, text, mtype = row
        chat_cat = classify_chat(subject, raw_jid)
        
        if category and category != "all" and chat_cat != category:
            continue
        
        chat_name = subject if subject else resolve_sender(c.execute("SELECT jid_row_id FROM chat WHERE _id = ?", (chat_id,)).fetchone()[0])
        sender_name = resolve_sender(sender_id, bool(from_me))
        
        dt_str = datetime.fromtimestamp(ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S")
        
        if not text and mtype != 0:
            type_desc = {
                1: "<Imagem ocultada>", 2: "<Áudio ocultado>", 3: "<Vídeo ocultado>",
                9: "<Documento anexado>", 5: "<Localização>", 8: "<Chamada>"
            }.get(mtype, "<Mídia/Evento>")
            msg_content = type_desc
        else:
            msg_content = text or ""
            
        if not msg_content:
            continue
            
        cat_group = results_by_cat[chat_cat]
        if chat_id not in cat_group:
            cat_group[chat_id] = {
                "name": chat_name,
                "raw_jid": raw_jid,
                "category": chat_cat,
                "messages": []
            }
        
        cat_group[chat_id]["messages"].append({
            "id": msg_id,
            "timestamp": ts,
            "datetime": dt_str,
            "sender": sender_name,
            "text": msg_content
        })
        total_msgs += 1
        
    return results_by_cat, total_msgs

def format_summary(results_by_cat, start_dt, end_dt, total_msgs):
    s = []
    s.append("=" * 65)
    s.append(f"📊 EXTRATO SEMANAL WHATSAPP TI ({start_dt.strftime('%d/%m/%Y')} a {end_dt.strftime('%d/%m/%Y')})")
    s.append("=" * 65)
    s.append(f"Total de mensagens registradas no período: {total_msgs}\n")
    
    labels = {
        "campo": "🛠️ Suporte ao Técnico de Campo (Tópico 6 do Relatório)",
        "interno": "💻 Suporte Interno / TI e Setores (Tópico 5 do Relatório)",
        "coordenacao": "👔 Coordenação de TI (Alinhamentos Isvi Neemias)",
        "incidentes": "🚨 Incidentes de Infraestrutura (Made4NOC / Tópico 4)",
        "outros": "💬 Outras Comunicações e Contatos Avulsos"
    }
    
    for cat_key, cat_title in labels.items():
        chats = results_by_cat.get(cat_key, {})
        cat_total = sum(len(c["messages"]) for c in chats.values())
        s.append(f"### {cat_title}: {cat_total} mensagens")
        for cid, cdata in chats.items():
            s.append(f"  - {cdata['name']}: {len(cdata['messages'])} mensagens")
        s.append("")
    
    s.append("=" * 65)
    return "\n".join(s)

def format_markdown(results_by_cat, start_dt, end_dt, total_msgs):
    md = []
    md.append(f"# 📱 Extrato Operacional de WhatsApp do Setor de TI")
    md.append(f"**Período:** {start_dt.strftime('%d/%m/%Y')} a {end_dt.strftime('%d/%m/%Y')}")
    md.append(f"**Total de Mensagens no Período:** {total_msgs}\n")
    
    labels = {
        "coordenacao": "1. Alinhamentos com a Coordenação de TI (Isvi Neemias)",
        "campo": "2. Suporte aos Técnicos de Campo (ServiceDesk, Projetos, Instalações)",
        "interno": "3. Suporte Interno / TI (Tecnologia TEN, Manutenção e Setores)",
        "incidentes": "4. Tratativas de Incidentes (Made4NOC / Infra)",
        "outros": "5. Outras Comunicações"
    }
    
    for cat_key, cat_title in labels.items():
        chats = results_by_cat.get(cat_key, {})
        if not chats:
            continue
        md.append(f"## {cat_title}\n")
        for cid, cdata in chats.items():
            md.append(f"### 📌 {cdata['name']} (`{len(cdata['messages'])} mensagens`)")
            md.append("```text")
            for m in cdata["messages"]:
                md.append(f"[{m['datetime']}] {m['sender']}: {m['text']}")
            md.append("```\n")
            
    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="Consulta mensagens do WhatsApp por período e categoria.")
    parser.add_argument("--start", required=True, help="Data inicial (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="Data final (YYYY-MM-DD)")
    parser.add_argument("--category", choices=["campo", "interno", "coordenacao", "incidentes", "all"], default="all", help="Categoria de interesse")
    parser.add_argument("--format", choices=["summary", "md", "txt", "json"], default="summary", help="Formato da saída")
    parser.add_argument("--output", help="Arquivo de saída opcional para salvar o resultado")
    
    args = parser.parse_args()
    
    try:
        start_dt = datetime.strptime(args.start, "%Y-%m-%d").replace(hour=0, minute=0, second=0)
        end_dt = datetime.strptime(args.end, "%Y-%m-%d").replace(hour=23, minute=59, second=59)
    except ValueError:
        print("[ERRO] Formato de data inválido! Use YYYY-MM-DD (ex.: 2026-09-07).")
        sys.exit(1)
        
    conn = load_database()
    results_by_cat, total_msgs = query_messages(conn, start_dt, end_dt, args.category)
    
    if args.format == "summary":
        out = format_summary(results_by_cat, start_dt, end_dt, total_msgs)
    elif args.format == "md":
        out = format_markdown(results_by_cat, start_dt, end_dt, total_msgs)
    elif args.format == "json":
        out = json.dumps({
            "periodo": {"inicio": args.start, "fim": args.end},
            "total_mensagens": total_msgs,
            "dados": results_by_cat
        }, ensure_ascii=False, indent=2)
    else: # txt
        out = format_markdown(results_by_cat, start_dt, end_dt, total_msgs)
        
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"[OK] Resultado exportado para: {args.output}")
    else:
        print(out)

if __name__ == "__main__":
    main()
