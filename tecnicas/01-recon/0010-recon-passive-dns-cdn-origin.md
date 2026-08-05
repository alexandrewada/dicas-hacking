---
id: "0010"
categoria: "01-recon"
familia: "recon-passive-dns"
slug: "cdn-origin"
angulo: "base"
mitre: ""
owasp: ""
tags: ["01-recon", "recon-passive-dns", "base"]
aliases: ["descoberta de origem atrás de CDN", "cdn-origin"]
---

# descoberta de origem atrás de CDN

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Detalhe

- Detalhe que pago pra ver: **Somente técnicas passivas/autorizadas; nunca force bypass fora do ROE**.

## Execução

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
# marcar dev-/staging- ; tag b7ac54 (cdn-origin)
```

## OpSec

Wildcard DNS gera falsos positivos massivos.

## Cuidados

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

## Fechamento

| | |
|---|---|
| Detecção | SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts. |
| Remediação | Inventário contínuo de ativos; remover staging exposto; DMARC p=reject;
segmentar DNS interno vs externo; alertas em mudanças de NS/MX. |
| Evidência | Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN. |

## Refs

- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
- [crt.sh — Certificate Transparency](https://crt.sh/)
- [HackTricks — DNS enumeration](https://book.hacktricks.xyz/network-services-pentesting/pentesting-dns)

## Relacionadas

- [descoberta de origem atrás de CDN — detecção](0390-recon-passive-dns-cdn-origin--detecao.md)
- [descoberta de origem atrás de CDN — path](0770-recon-passive-dns-cdn-origin--path.md)
- [clustering por ASN e netblocks](0004-recon-passive-dns-asn-cluster.md)
- [via Certificate Transparency (crt.sh)](0001-recon-passive-dns-crtsh.md)
- [auditoria DMARC/BIMI](0007-recon-passive-dns-dmarc-policy.md)
- [infraestrutura de e-mail e relays](0009-recon-passive-dns-mx-infra.md)