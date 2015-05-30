# teste autorizado de AXFR

**A05:2021 Security Misconfiguration / A01 Broken Access (superficie)** · `T1590 Gather Victim Network Information`

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Como eu faço

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## Sinal / query

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag abf2ca (zone-transfer)
```

## Diferencial desta nota

- AXFR aberto é misconfig clássica; documente nameserver e resposta completa.

Antes de Critical em teste autorizado de AXFR, confiro se a telemetria que eu cobraria reagiria — SIEM/DNS logs: picos de consultas a subdomínios inexistentes. Certificate Transparency monitoring (ex.: certstream) para.

## Onde já errei

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Entrega

- blue: SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.
- fix: Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.
- proof: Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

## Refs

- OWASP Testing Guide WSTG-INFO
- MITRE ATT&CK T1590
- RFC 1035