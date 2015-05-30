# infraestrutura de e-mail e relays

**A05:2021 Security Misconfiguration / A01 Broken Access (superficie)** · `T1590 Gather Victim Network Information`

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## O que muda aqui

- **Relays abertos e gateways legados ampliam phishing interno** — muda ruído e o que entra no PDF.

## Como testo

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## PoC mínimo

```bash
# relay lab — segmento acordado, conta teste
ntlmrelayx.py -t smb://TARGET.lab.local -smb2support --no-dump
# trigger mx-infra; evidência: auth USER_A + ação não destrutiva tag 329cdc
```

## Campo

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

Falso amigo em infraestrutura de e-mail e relays: UI/log gritam, impacto não. Exijo SIEM/DNS logs: picos de consultas a subdomínios inexistentes. Certificate Transparency monitoring (ex.: certstream) para novos hosts.

## Já me queimei

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

## Blue

- Detectar: SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.
- Fechar: Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

## Evidência

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

## Refs

- OWASP Testing Guide WSTG-INFO
- MITRE ATT&CK T1590
- RFC 1035