---
id: "0023"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "linkedin-pretext"
angulo: "base"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "base", "t1589"]
aliases: ["pretext a partir de LinkedIn", "linkedin-pretext"]
---

# pretext a partir de LinkedIn

**A07 Identification and Authentication Failures (contexto)** · `T1589 Gather Victim Identity Information`

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

**Variante:** **Somente se SE estiver no ROE** — muda ruído e o que entra no PDF.

**Método**

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag eef9f1 (linkedin-pretext)
```

**Freio:** Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.

Falso amigo em pretext a partir de LinkedIn: UI/log gritam, impacto não. Exijo Monitorar menções à marca.

Detecto via: Monitorar menções à marca; alertas de credential stuffing; DMARC.

Corrijo com: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.

Levo no report: Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [pretext a partir de LinkedIn — detecção](0403-recon-osint-people-linkedin-pretext--detecao.md)
- [pretext a partir de LinkedIn — path](0783-recon-osint-people-linkedin-pretext--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)