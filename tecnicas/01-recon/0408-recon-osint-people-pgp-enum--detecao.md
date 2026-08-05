---
id: "0408"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "pgp-enum"
angulo: "detecao"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "detecao", "t1589"]
aliases: ["enumeração via diretórios PGP", "pgp-enum", "pgp-enum-detecao"]
---

# enumeração via diretórios PGP — detecção

Gap de detecção em `T1589 Gather Victim Identity Information` / enumeração via diretórios PGP. PoC mínimo, telemetria ligada.

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Hipótese

- **E-mails históricos ainda úteis** — muda ruído e o que entra no PDF.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## Exemplo

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — pgp-enum 6e814c
```

## Sinal

Monitorar menções à marca; alertas de credential stuffing; DMARC.

## Freio

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Evidência

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [enumeração via diretórios PGP](0028-recon-osint-people-pgp-enum.md)
- [enumeração via diretórios PGP — path](0788-recon-osint-people-pgp-enum--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)