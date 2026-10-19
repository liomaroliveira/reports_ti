#!/usr/bin/env python3
"""
Script Aprimorado de Mapeamento, Descoberta e Auditoria de Subdomínios
Alvo: *.teninternet.com.br
Objetivo: Mapear 100% dos apontamentos DNS ativos, identificar tecnologias e auditar riscos de segurança.
Uso: python3 investigation/mapear_subdominios_teninternet.py
"""

import socket
import urllib.request
import urllib.error
import json
import ssl
import sys
import re
from concurrent.futures import ThreadPoolExecutor

DOMAIN = "teninternet.com.br"

# Wordlist expandida com mais de 160 termos corporativos, telecom, provedor e docker
WORDLIST = [
    # Sistemas Internos e Departamentos
    "compras", "estoque", "frota", "escala", "ciclos", "catalogo", "controle-testes",
    "pendencias", "mwsistema", "mwapi", "autotickets", "guardian", "mundialehistory",
    "docs", "wiki", "drive", "cloud", "nextcloud", "sso", "auth", "login", "admin",
    "central", "contratos", "suporte", "atendimento", "chamados", "tickets", "voalle",
    "sac", "noc", "bi", "metabase", "grafana", "zabbix", "prtg", "speedtest", "radius",
    "synsuite", "webmail", "mail", "cpanel", "play", "pague", "indique", "portal",
    "portal-staging", "erp", "erp-staging", "homologa", "homolog", "dev", "staging",
    "teste", "testes", "qa", "prod", "api", "app", "dashboard", "gestao", "financeiro",
    "fiscal", "contabil", "faturamento", "cobranca", "boleto", "rh", "pessoal", "dp",
    "ponto", "beneficios", "ti", "infra", "infraestrutura", "glpi", "jira", "confluence",
    "backup", "backups", "git", "gitlab", "jenkins", "vpn", "wireguard", "openvpn",
    "status", "uptime", "monitor", "powerbi", "superset", "redmine", "hub", "bot",
    "whatsapp", "chat", "crm", "vendas", "comercial", "cliente", "assinante", "minhaten",
    "meuapp", "id", "identity", "traefik", "nginx", "proxy", "gateway", "edge", "core",
    "borda", "pop", "olt", "onu", "mikrotik", "huawei", "cisco", "juniper", "ix", "asn",
    "bgp", "radius1", "radius2", "dns1", "dns2", "ns1", "ns2", "ns3", "ns4", "mx1",
    "mx2", "smtp", "imap", "pop3", "mail2", "intranet", "interno", "colaborador",
    "funcionarios", "ponto", "feed", "notificacoes", "webhook", "webhooks", "integracao",
    "fila", "redis", "elastic", "kibana", "graylog", "loki", "prometheus", "tempo",
    "minio", "s3", "storage", "files", "download", "downloads", "upload", "uploads",
    "midia", "static", "cdn", "assets", "media", "img", "images", "seguranca", "cyber",
    "security", "siem", "wazuh", "suricata", "snort", "firewall", "pfsense", "opnsense",
    "fortigate", "flashman", "made4flow", "bloqueado", "bloqueio", "autodiscover",
    "cpcalendars", "cpcontacts"
]

# Adicionar nós da infraestrutura Docker
DOCKER_NODES = ["docker-01", "docker-02"]
DOCKER_CONTAINERS = [
    "portainer", "pgadmin", "n8n", "n8n-main", "baserow", "rabbitmq", "smokeping",
    "redis", "postgres", "mongo", "grafana", "zabbix", "uptime", "traefik", "nginx",
    "vault", "minio", "krill", "easygrafana", "easyportainer", "easyzabbix"
]

for node in DOCKER_NODES:
    for c in DOCKER_CONTAINERS:
        WORDLIST.append(f"{c}.{node}")

def fetch_hackertarget(domain):
    subs = set()
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Audit-Bot)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            for line in content.splitlines():
                if "," in line:
                    sub = line.split(",")[0].strip().lower()
                    if domain in sub:
                        subs.add(sub)
    except Exception as e:
        print(f"[-] Erro HackerTarget: {e}", file=sys.stderr)
    return subs

def fetch_rapiddns(domain):
    subs = set()
    url = f"https://rapiddns.io/s/{domain}?rim=1"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Audit-Bot)"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            matches = re.findall(r"[a-zA-Z0-9\.\-]+\." + re.escape(domain), content)
            for m in matches:
                subs.add(m.strip().lower())
    except Exception as e:
        print(f"[-] Erro RapidDNS: {e}", file=sys.stderr)
    return subs

def resolve_dns(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception:
        return None

def audit_http(hostname):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    info = {
        "status": "Porta Fechada",
        "protocol": "N/D",
        "server": "N/D",
        "title": "",
        "uses_supabase": False,
        "supabase_url": None,
        "env_exposed": False,
        "git_exposed": False,
        "security_headers": {}
    }

    for proto in ["https", "http"]:
        url = f"{proto}://{hostname}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Defensive-Audit)"})
        try:
            with urllib.request.urlopen(req, timeout=6, context=ctx) as resp:
                info["status"] = resp.status
                info["protocol"] = proto.upper()
                info["server"] = resp.headers.get("Server", "N/D")
                body = resp.read().decode("utf-8", errors="ignore")

                # Extrair título da página
                m_title = re.search(r"<title[^>]*>(.*?)</title>", body, re.IGNORECASE | re.DOTALL)
                if m_title:
                    info["title"] = m_title.group(1).strip().replace("\n", " ")[:40]

                # Verificar se consome Supabase
                m_supa = re.search(r"https://([a-z0-9]+)\.supabase\.co", body)
                if m_supa:
                    info["uses_supabase"] = True
                    info["supabase_url"] = m_supa.group(0)

                # Se conectou com sucesso, para
                break
        except urllib.error.HTTPError as e:
            info["status"] = e.code
            info["protocol"] = proto.upper()
            info["server"] = e.headers.get("Server", "N/D")
            break
        except Exception:
            continue

    # Verificação defensiva de arquivos sensíveis se a porta web estiver aberta
    if isinstance(info["status"], int) and info["status"] < 500:
        # Check .env
        try:
            req_env = urllib.request.Request(f"https://{hostname}/.env", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_env, timeout=3, context=ctx) as r:
                if r.status == 200:
                    c_type = r.headers.get("Content-Type", "")
                    content = r.read().decode("utf-8", errors="ignore")
                    if "text/html" not in c_type and ("APP_" in content or "DB_" in content):
                        info["env_exposed"] = True
        except:
            pass

        # Check .git
        try:
            req_git = urllib.request.Request(f"https://{hostname}/.git/HEAD", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req_git, timeout=3, context=ctx) as r:
                if r.status == 200:
                    content = r.read().decode("utf-8", errors="ignore")
                    if "ref: refs/" in content:
                        info["git_exposed"] = True
        except:
            pass

    return info

def main():
    print("=" * 80)
    print(f" MAPEAMENTO E AUDITORIA DEFENSIVA AMPLIADA: *.{DOMAIN}")
    print("=" * 80)

    candidates = set()

    print("[1/3] Coletando subdomínios de bases de inteligência passiva...")
    ht_subs = fetch_hackertarget(DOMAIN)
    candidates.update(ht_subs)
    print(f"      + HackerTarget: {len(ht_subs)} subdomínios")

    rd_subs = fetch_rapiddns(DOMAIN)
    candidates.update(rd_subs)
    print(f"      + RapidDNS: {len(rd_subs)} subdomínios")

    print("[2/3] Adicionando wordlist de termos operacionais, ISP e Docker...")
    for w in WORDLIST:
        candidates.add(f"{w}.{DOMAIN}")
    print(f"      + Total de alvos para resolução DNS: {len(candidates)}")

    print("[3/3] Resolvendo DNS e auditando serviços web...")
    print("-" * 80)
    print(f"{'SUBDOMÍNIO':<36} | {'IP RESOLVIDO':<15} | {'STATUS':<10} | {'SISTEMA/TÍTULO'}")
    print("-" * 80)

    live_hosts = []

    def process_subdomain(sub):
        ip = resolve_dns(sub)
        if ip:
            audit = audit_http(sub)
            return {
                "subdomain": sub,
                "ip": ip,
                "status": audit["status"],
                "protocol": audit["protocol"],
                "server": audit["server"],
                "title": audit["title"],
                "uses_supabase": audit["uses_supabase"],
                "supabase_url": audit["supabase_url"],
                "env_exposed": audit["env_exposed"],
                "git_exposed": audit["git_exposed"]
            }
        return None

    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(process_subdomain, sorted(candidates))
        for r in results:
            if r:
                live_hosts.append(r)
                stat_str = f"{r['protocol']} {r['status']}" if isinstance(r['status'], int) else str(r['status'])
                title_str = r['title'] if r['title'] else (r['server'] if r['server'] != 'N/D' else '-')
                supa_flag = " [SUPABASE]" if r['uses_supabase'] else ""
                print(f"{r['subdomain']:<36} | {r['ip']:<15} | {stat_str:<10} | {title_str[:22]}{supa_flag}")

    print("-" * 80)
    print(f"[+] Total de apontamentos ativos confirmados: {len(live_hosts)}")

    output_file = "investigation/subdominios_ativos.json"
    with open(output_file, "w", encoding="utf-8") as fp:
        json.dump(live_hosts, fp, indent=2, ensure_ascii=False)
    print(f"[+] Relatório completo estruturado salvo em: {output_file}")

if __name__ == "__main__":
    main()
