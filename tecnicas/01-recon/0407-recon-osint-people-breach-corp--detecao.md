---
id: "0407"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "breach-corp"
angulo: "detecao"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "detecao", "t1589"]
aliases: ["correlação com breaches corporativos", "breach-corp", "breach-corp-detecao"]
---

# correlação com breaches corporativos — detecção

Se o SOC não vê correlação com breaches corporativos, o finding é de cobertura, não de ego ofensivo.

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Hipótese

- Detalhe que pago pra ver: **Priorize spraying com MFA bypass research ética**.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — breach-corp 283d00
```

## Sinal

Monitorar menções à marca; alertas de credential stuffing; DMARC.

## Freio

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Evidência

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [correlação com breaches corporativos — path](0787-recon-osint-people-breach-corp--path.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)
- [pretext a partir de LinkedIn](0023-recon-osint-people-linkedin-pretext.md)