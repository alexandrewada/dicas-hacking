---
id: "0790"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "whois-privacy"
angulo: "path"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "path", "t1589"]
aliases: ["WHOIS e contatos de abuse", "whois-privacy", "whois-privacy-path"]
---

# WHOIS e contatos de abuse — path

WHOIS e contatos de abuse como pivô. Path curto > monte de finding isolado.

## Papel

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Por que pivota

- Se não validar **Útil para reporte responsável, não só ataque**, a nota fica genérica.

## Cadeia

1. Entrada (escopo)
2. Pivô: WHOIS e contatos de abuse
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## Sinal / query

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 3962cd (whois-privacy)
```

## Freio

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

## No caminho

Detectar: Monitorar menções à marca; alertas de credential stuffing; DMARC.

Remediar: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.

## Prova

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [WHOIS e contatos de abuse](0030-recon-osint-people-whois-privacy.md)
- [WHOIS e contatos de abuse — detecção](0410-recon-osint-people-whois-privacy--detecao.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)