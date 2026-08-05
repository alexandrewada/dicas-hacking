---
id: "0386"
categoria: "01-recon"
familia: "recon-passive-dns"
slug: "srv-enum"
angulo: "detecao"
mitre: "T1590"
owasp: ""
tags: ["01-recon", "recon-passive-dns", "detecao", "t1590"]
aliases: ["enumeração de registros SRV", "srv-enum", "srv-enum-detecao"]
---

# enumeração de registros SRV — detecção

Se o SOC não vê enumeração de registros SRV, o finding é de cobertura, não de ego ofensivo.

## Contexto

Em engajamentos autorizados, DNS é frequentemente a primeira fonte de verdade sobre a superfície externa.
Registros A/AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC), NS e histórico (SecurityTrails, VirusTotal, crt.sh)
revelam hosts esquecidos, ambientes de staging e cadeias de CDN.
O objetivo não é 'encontrar tudo no Google', e sim construir um **grafo de ativos** correlacionável com certificados,
ASN e padrões de nomenclatura corporativa.

## Hipótese

- **SRV `_ldap._tcp`, `_kerberos`, `_sip` revelam identidade e VoIP** — muda ruído e o que entra no PDF.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Coleto domínio seed autorizado e wildcards do escopo.
2. Extrair SANs de certificados via crt.sh / Censys (somente leitura pública).
3. Resolver passivamente; marcar NXDOMAIN vs wildcards.
4. Agrupar por ASN e CDN; isolar origin IPs quando política permitir.
5. Cruzar com WHOIS histórico e mudanças de NS (hijack residual).
6. Entregar inventário com criticidade e dono presumido.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — srv-enum 101da6
```

## Sinal

SIEM/DNS logs: picos de consultas a subdomínios inexistentes.
Certificate Transparency monitoring (ex.: certstream) para novos hosts.

## Freio

Wildcard DNS gera falsos positivos massivos.
Subdomínios em CDN não implicam origem vulnerável.
Dados públicos podem estar desatualizados — valide no escopo ativo só com autorização.

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

## Evidência

Lista de FQDN + fonte + timestamp; evidência de certificado; mapa ASN.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1590](https://attack.mitre.org/techniques/T1590/)
- [OWASP WSTG — Information Gathering](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/README)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [RFC 1035 — DNS](https://www.rfc-editor.org/rfc/rfc1035)
- [crt.sh — Certificate Transparency](https://crt.sh/)

## Relacionadas

- [enumeração de registros SRV](0006-recon-passive-dns-srv-enum.md)
- [enumeração de registros SRV — path](0766-recon-passive-dns-srv-enum--path.md)
- [clustering por ASN e netblocks](0004-recon-passive-dns-asn-cluster.md)
- [descoberta de origem atrás de CDN](0010-recon-passive-dns-cdn-origin.md)
- [via Certificate Transparency (crt.sh)](0001-recon-passive-dns-crtsh.md)
- [auditoria DMARC/BIMI](0007-recon-passive-dns-dmarc-policy.md)