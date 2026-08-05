---
id: "0004"
categoria: "01-recon"
familia: "recon-passive-dns"
slug: "asn-cluster"
angulo: "base"
mitre: "T1590"
owasp: ""
tags: ["01-recon", "recon-passive-dns", "base", "t1590"]
aliases: ["clustering por ASN e netblocks", "asn-cluster"]
---

# clustering por ASN e netblocks

**A05:2021 Security Misconfiguration / A01 Broken Access (superficie)** · `T1590 Gather Victim Network Information`

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## O que muda aqui

- **Agrupe ranges e priorize netblocks sem WAF corporativo** — muda ruído e o que entra no PDF.

## Como testo

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## Exemplo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 2961d8 (asn-cluster)
```

## Campo

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

clustering por ASN e netblocks: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: SIEM/DNS logs: picos de consultas a subdomínios inexistentes. Certificate Transparency monitoring (e.

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

- [MITRE ATT&CK T1590](https://attack.mitre.org/techniques/T1590/)
- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
- [crt.sh — Certificate Transparency](https://crt.sh/)

## Relacionadas

- [clustering por ASN e netblocks — detecção](0384-recon-passive-dns-asn-cluster--detecao.md)
- [clustering por ASN e netblocks — path](0764-recon-passive-dns-asn-cluster--path.md)
- [descoberta de origem atrás de CDN](0010-recon-passive-dns-cdn-origin.md)
- [via Certificate Transparency (crt.sh)](0001-recon-passive-dns-crtsh.md)
- [auditoria DMARC/BIMI](0007-recon-passive-dns-dmarc-policy.md)
- [infraestrutura de e-mail e relays](0009-recon-passive-dns-mx-infra.md)