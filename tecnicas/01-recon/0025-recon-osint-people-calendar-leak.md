---
id: "0025"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "calendar-leak"
angulo: "base"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "base", "t1589"]
aliases: ["vazamento de calendários/ICS", "calendar-leak"]
---

# vazamento de calendários/ICS

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Detalhe

- **Reuniões e salas como pretext** — muda ruído e o que entra no PDF.

## Execução

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 2edc47 (calendar-leak)
```

## OpSec

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.

## Cuidados

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

## Fechamento

| | |
|---|---|
| Detecção | Monitorar menções à marca; alertas de credential stuffing; DMARC. |
| Remediação | Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts. |
| Evidência | Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável. |

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [vazamento de calendários/ICS — detecção](0405-recon-osint-people-calendar-leak--detecao.md)
- [vazamento de calendários/ICS — path](0785-recon-osint-people-calendar-leak--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)
- [pretext a partir de LinkedIn](0023-recon-osint-people-linkedin-pretext.md)