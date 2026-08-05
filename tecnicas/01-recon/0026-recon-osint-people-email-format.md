---
id: "0026"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "email-format"
angulo: "base"
mitre: ""
owasp: ""
tags: ["01-recon", "recon-osint-people", "base"]
aliases: ["inferência de formato de e-mail", "email-format"]
---

# inferência de formato de e-mail

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Detalhe

- Se não validar **Valide com cuidado para não spammar**, a nota fica genérica.

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
# marcar dev-/staging- ; tag 86f647 (email-format)
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

- [OSINT Framework](https://osintframework.com/)
- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [inferência de formato de e-mail — detecção](0406-recon-osint-people-email-format--detecao.md)
- [inferência de formato de e-mail — path](0786-recon-osint-people-email-format--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)
- [pretext a partir de LinkedIn](0023-recon-osint-people-linkedin-pretext.md)