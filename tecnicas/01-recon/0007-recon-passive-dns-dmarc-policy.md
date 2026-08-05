---
id: "0007"
categoria: "01-recon"
familia: "recon-passive-dns"
slug: "dmarc-policy"
angulo: "base"
mitre: "T1590"
owasp: ""
tags: ["01-recon", "recon-passive-dns", "base", "t1590"]
aliases: ["auditoria DMARC/BIMI", "dmarc-policy"]
---

# auditoria DMARC/BIMI

`T1590 Gather Victim Network Information`

## Por que importa

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Variante

- Política fraca habilita phishing; trate como finding de email security.
- include órfão = spoof. checkdmarc + proposta (-all / reject).

## Passo a passo

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
# marcar dev-/staging- ; tag 9cc12c (dmarc-policy)
```

## Nota de operador

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Armadilha

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

Falso amigo em auditoria DMARC/BIMI: UI/log gritam, impacto não. Exijo SIEM/DNS logs: picos de consultas a subdomínios inexistentes. Certificate Transparency monitoring (ex.: certstream) para novos hosts.

## Depois

Detecção — SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

Remediação — Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX.

No PDF — Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

## Refs

- [MITRE ATT&CK T1590](https://attack.mitre.org/techniques/T1590/)
- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
- [crt.sh — Certificate Transparency](https://crt.sh/)

## Relacionadas

- [auditoria DMARC/BIMI — detecção](0387-recon-passive-dns-dmarc-policy--detecao.md)
- [auditoria DMARC/BIMI — path](0767-recon-passive-dns-dmarc-policy--path.md)
- [clustering por ASN e netblocks](0004-recon-passive-dns-asn-cluster.md)
- [descoberta de origem atrás de CDN](0010-recon-passive-dns-cdn-origin.md)
- [via Certificate Transparency (crt.sh)](0001-recon-passive-dns-crtsh.md)
- [infraestrutura de e-mail e relays](0009-recon-passive-dns-mx-infra.md)