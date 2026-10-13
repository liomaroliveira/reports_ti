#!/usr/bin/env python3
"""
Script de automação para descriptografar e exportar todas as conversas do WhatsApp Business
a partir do arquivo msgstore.db.crypt15 utilizando a chave de 64 dígitos.
Gera arquivos .txt individuais por conversa e um índice geral em JSON.
"""

import os
import sys
import re
import json
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BKP_DIR = os.path.join(BASE_DIR, "bkp_64digits")
DB_PATH = os.path.join(BKP_DIR, "msgstore.db")
OUTPUT_DIR = os.path.join(BASE_DIR, "conversas_exportadas")

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.isfile(DB_PATH):
    print(f"Erro: Banco de dados descriptografado não encontrado em: {DB_PATH}")
    sys.exit(1)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Mapeamento de contatos conhecidos (Diretrizes do Setor de TI)
known = {
    "[telefone removido]": "Isvi Neemias (Coordenação TI)",
    "[telefone removido]": "Liomar Oliveira",
    "[telefone removido]": "Liomar Oliveira",
    "[telefone removido]": "Isac Costa",
    "[telefone removido]": "Isac Costa",
    "[telefone removido]": "David Brasil",
    "[telefone removido]": "David Brasil",
    "[telefone removido]": "Setor TI Ten",
    "[telefone removido]": "Setor TI Ten",
}

# Enriquecimento com vCards extraídos
vcard_dir = os.path.join(BKP_DIR, "exported_txt", "WhatsApp", "vCards")
if os.path.isdir(vcard_dir):
    for f in os.listdir(vcard_dir):
        if f.endswith(".vcf"):
            path = os.path.join(vcard_dir, f)
            try:
                content = open(path, "r", encoding="utf-8", errors="ignore").read()
                name_match = re.search(r"FN:(.*)", content)
                tel_match = re.search(r"TEL.*:(.*)", content)
                name = name_match.group(1).strip() if name_match else f[:-4]
                if tel_match and name:
                    tel = re.sub(r"\D", "", tel_match.group(1))
                    if len(tel) >= 8 and tel not in known:
                        known[tel] = name
            except Exception:
                pass

# Carregar JIDs
jid_rows = c.execute("SELECT _id, user, server, raw_string FROM jid").fetchall()
jids = {r[0]: {"user": r[1], "server": r[2], "raw": r[3]} for r in jid_rows}

# Mapeamento de LID para JID
lid_map = {}
for r in c.execute("SELECT lid_row_id, jid_row_id FROM jid_map").fetchall():
    lid_map[r[0]] = r[1]

def get_name(jid_id, is_from_me=False):
    if is_from_me:
        return "Você (Liomar TI)"
    if not jid_id or jid_id not in jids:
        return "Desconhecido"
    if jid_id in lid_map:
        jid_id = lid_map[jid_id]
    info = jids.get(jid_id, {})
    user = info.get("user", "")
    if user in known:
        return known[user]
    # Suffix match (últimos 8 dígitos para cobrir variações de 9º dígito)
    for k, v in known.items():
        if user and len(user) >= 8 and len(k) >= 8:
            if user[-8:] == k[-8:]:
                return v
    return user if user else info.get("raw", "Desconhecido")

def sanitize(name):
    clean = re.sub(r"[\\/*?:\":<>|]", "_", name).strip()
    return clean[:80]

chats = c.execute("""
    SELECT c._id, c.subject, c.jid_row_id, j.user, j.server, j.raw_string
    FROM chat c
    JOIN jid j ON c.jid_row_id = j._id
""").fetchall()

print(f"Processando {len(chats)} conversas...")
chat_index = []
exported_count = 0
total_messages = 0

for chat in chats:
    chat_id, subject, jid_id, user, server, raw = chat
    is_group = bool(subject) or (raw and "@g.us" in raw)
    chat_name = subject if subject else get_name(jid_id)
    
    msgs = c.execute("""
        SELECT m.timestamp, m.from_me, m.sender_jid_row_id, m.text_data, m.message_type
        FROM message m
        WHERE m.chat_row_id = ?
        ORDER BY m.timestamp ASC
    """, (chat_id,)).fetchall()
    
    if not msgs:
        continue
    
    file_title = f"Conversa do WhatsApp com {sanitize(chat_name)}.txt"
    file_path = os.path.join(OUTPUT_DIR, file_title)
    
    valid_msgs = 0
    first_ts = None
    last_ts = None
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"--- Histórico: {chat_name} ({raw}) ---\n\n")
        for m in msgs:
            ts, from_me, sender_id, text, mtype = m
            if not ts:
                continue
            if first_ts is None:
                first_ts = ts
            last_ts = ts
            
            dt = datetime.fromtimestamp(ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S")
            sender = get_name(sender_id, bool(from_me))
            
            if text:
                f.write(f"[{dt}] {sender}: {text}\n")
                valid_msgs += 1
            elif mtype != 0:
                type_desc = {
                    1: "<Imagem ocultada>",
                    2: "<Áudio ocultado>",
                    3: "<Vídeo ocultado>",
                    9: "<Documento anexado>",
                    5: "<Localização>",
                    8: "<Chamada de voz/vídeo>"
                }.get(mtype, "<Mídia/Evento>")
                f.write(f"[{dt}] {sender}: {type_desc}\n")
                valid_msgs += 1
    
    if valid_msgs > 0:
        exported_count += 1
        total_messages += valid_msgs
        chat_index.append({
            "chat_id": chat_id,
            "name": chat_name,
            "raw_jid": raw,
            "is_group": is_group,
            "message_count": valid_msgs,
            "first_message": datetime.fromtimestamp(first_ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S") if first_ts else None,
            "last_message": datetime.fromtimestamp(last_ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S") if last_ts else None,
            "file": file_title
        })

# Salvar índice geral
index_path = os.path.join(OUTPUT_DIR, "indice_conversas.json")
with open(index_path, "w", encoding="utf-8") as f:
    json.dump({
        "data_exportacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "total_conversas": exported_count,
        "total_mensagens": total_messages,
        "conversas": sorted(chat_index, key=lambda x: x["message_count"], reverse=True)
    }, f, ensure_ascii=False, indent=2)

print(f"Exportação finalizada com sucesso!")
print(f"- Conversas ativas: {exported_count}")
print(f"- Mensagens totais: {total_messages}")
print(f"- Arquivos salvos em: {OUTPUT_DIR}")
print(f"- Índice gerado em: {index_path}")
