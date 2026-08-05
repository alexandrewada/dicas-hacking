---
id: "0024"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "paste-sites"
angulo: "base"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "base", "t1589"]
aliases: ["monitoramento de pastes", "paste-sites"]
---

# monitoramento de pastes

**A07 Identification and Authentication Failures (contexto)** · `T1589 Gather Victim Identity Information`

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Como eu faço

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## PoC mínimo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 7fe91f (paste-sites)
```

## Diferencial desta nota

- **IOCs de vazamento recentes.** Sem isso o playbook da família mente.

Já abri High demais em monitoramento de pastes por sintoma sem efeito. Cruzei com: Monitorar menções à marca; alertas de credential stuffing; DMARC. Sem side-effect, baixo.

## Onde já errei

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

## Entrega

- blue: Monitorar menções à marca; alertas de credential stuffing; DMARC.
- fix: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.
- proof: Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [monitoramento de pastes — detecção](0404-recon-osint-people-paste-sites--detecao.md)
- [monitoramento de pastes — path](0784-recon-osint-people-paste-sites--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)