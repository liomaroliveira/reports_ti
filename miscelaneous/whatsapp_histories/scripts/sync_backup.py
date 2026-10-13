#!/usr/bin/env python3
"""
Script de sincronização semanal do WhatsApp Business para o setor de TI (Ten Internet).
Descriptografa automaticamente o arquivo msgstore.db.crypt15 mais recente em 'input/'
e atualiza o banco de dados mestre em 'database/msgstore.db'.
"""

import os
import sys
import glob
import sqlite3
import subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "input")
DB_DIR = os.path.join(BASE_DIR, "database")
OUTPUT_DB = os.path.join(DB_DIR, "msgstore.db")
KEY_FILE = os.path.join(BASE_DIR, "key_64digits.txt")
VENV_BIN = os.path.join(os.path.dirname(BASE_DIR), ".venv", "bin")
WADECRYPT_BIN = os.path.join(VENV_BIN, "wadecrypt")

os.makedirs(DB_DIR, exist_ok=True)
os.makedirs(INPUT_DIR, exist_ok=True)

def get_key():
    if not os.path.isfile(KEY_FILE):
        print(f"[ERRO] Arquivo de chave não encontrado em: {KEY_FILE}")
        sys.exit(1)
    with open(KEY_FILE, "r", encoding="utf-8") as f:
        key = f.read().strip()
    if len(key) != 64:
        print(f"[ERRO] Chave inválida! Esperava 64 caracteres hexadecimais, obteve {len(key)}.")
        sys.exit(1)
    return key

def find_latest_backup():
    candidates = []
    for pattern in ["*.crypt15", "*.crypt14", "*.crypt12"]:
        candidates.extend(glob.glob(os.path.join(INPUT_DIR, pattern)))
    if not candidates:
        print(f"[ERRO] Nenhum arquivo .crypt15 ou .crypt14 encontrado em: {INPUT_DIR}")
        print("Por favor, copie o novo backup do celular para a pasta 'input/' e tente novamente.")
        sys.exit(1)
    # Ordenar por data de modificação
    candidates.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return candidates[0]

def decrypt_backup(key, input_file, output_file):
    print(f"[*] Backup localizado: {os.path.basename(input_file)} ({os.path.getsize(input_file) / (1024*1024):.2f} MB)")
    print(f"[*] Descriptografando com a chave de 64 dígitos...")
    
    cmd = [WADECRYPT_BIN, key, input_file, output_file]
    if not os.path.isfile(WADECRYPT_BIN):
        # Fallback para execução via python do sistema caso o venv não esteja no path
        cmd = ["wadecrypt", key, input_file, output_file]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0 or not os.path.isfile(output_file) or os.path.getsize(output_file) == 0:
        print(f"[ERRO] Falha na descriptografia:")
        print(result.stdout)
        print(result.stderr)
        sys.exit(1)
    print(f"[OK] Banco SQLite gerado com sucesso: {output_file} ({os.path.getsize(output_file) / (1024*1024):.2f} MB)")

def inspect_database(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    total_chats = c.execute("SELECT count(*) FROM chat").fetchone()[0]
    total_msgs = c.execute("SELECT count(*) FROM message").fetchone()[0]
    
    latest_ts = c.execute("SELECT max(timestamp) FROM message").fetchone()[0]
    latest_dt = datetime.fromtimestamp(latest_ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S") if latest_ts else "N/A"
    
    earliest_ts = c.execute("SELECT min(timestamp) FROM message WHERE timestamp > 0").fetchone()[0]
    earliest_dt = datetime.fromtimestamp(earliest_ts / 1000.0).strftime("%d/%m/%Y %H:%M:%S") if earliest_ts else "N/A"
    
    print("\n" + "="*60)
    print("📊 RESUMO DA BASE DO WHATSAPP ATUALIZADA")
    print("="*60)
    print(f"• Total de conversas cadastradas: {total_chats}")
    print(f"• Total de mensagens arquivadas: {total_msgs}")
    print(f"• Período das mensagens: de {earliest_dt} até {latest_dt}")
    
    print("\n🔍 Destaque dos Canais Estratégicos de TI:")
    key_channels = [
        "ServiceDesk Suporte ao técnico",
        "Tecnologia TEN",
        "Projetos TEN - Apoio ao Técnico",
        "All Inclusive - TEN",
        "[Made4NOC] TEN INTERNET LTDA | PREMIUM",
        "Manutenção de computadores"
    ]
    for ch in key_channels:
        row = c.execute("""
            SELECT count(m._id), max(m.timestamp)
            FROM chat c
            LEFT JOIN message m ON m.chat_row_id = c._id
            WHERE c.subject = ?
        """, (ch,)).fetchone()
        cnt = row[0] if row else 0
        l_ts = row[1] if row and row[1] else None
        l_dt = datetime.fromtimestamp(l_ts / 1000.0).strftime("%d/%m %H:%M") if l_ts else "N/A"
        print(f"  - {ch}: {cnt} msgs (Última atividade: {l_dt})")
    
    print("="*60 + "\n")

def main():
    key = get_key()
    latest_bkp = find_latest_backup()
    decrypt_backup(key, latest_bkp, OUTPUT_DB)
    inspect_database(OUTPUT_DB)

if __name__ == "__main__":
    main()
