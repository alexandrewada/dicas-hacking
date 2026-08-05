---
id: "0768"
categoria: "01-recon"
familia: "recon-passive-dns"
slug: "ptr-recon"
angulo: "path"
mitre: "T1590"
owasp: ""
tags: ["01-recon", "recon-passive-dns", "path", "t1590"]
aliases: ["reconhecimento via PTR reverso", "ptr-recon", "ptr-recon-path"]
---

# reconhecimento via PTR reverso — path

reconhecimento via PTR reverso como pivô. Path curto > monte de finding isolado.

## Papel

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Por que pivota

- **PTR em ranges cloud frequentemente vazam hostnames internos** — muda ruído e o que entra no PDF.

## Cadeia

1. Entrada (escopo)
2. Pivô: reconhecimento via PTR reverso
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag ae9962 (ptr-recon)
```

## Freio

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

## No caminho

Detectar: SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

Remediar: Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

## Prova

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Refs

- [MITRE ATT&CK T1590](https://attack.mitre.org/techniques/T1590/)
- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
- [crt.sh — Certificate Transparency](https://crt.sh/)

## Relacionadas

- [reconhecimento via PTR reverso](0008-recon-passive-dns-ptr-recon.md)
- [reconhecimento via PTR reverso — detecção](0388-recon-passive-dns-ptr-recon--detecao.md)
- [clustering por ASN e netblocks](0004-recon-passive-dns-asn-cluster.md)
- [descoberta de origem atrás de CDN](0010-recon-passive-dns-cdn-origin.md)
- [via Certificate Transparency (crt.sh)](0001-recon-passive-dns-crtsh.md)
- [auditoria DMARC/BIMI](0007-recon-passive-dns-dmarc-policy.md)