---
id: "0022"
categoria: "01-recon"
familia: "recon-osint-people"
slug: "metadata-pdf"
angulo: "base"
mitre: "T1589"
owasp: ""
tags: ["01-recon", "recon-osint-people", "base", "t1589"]
aliases: ["metadata em PDFs corporativos", "metadata-pdf"]
---

# metadata em PDFs corporativos

**A07 Identification and Authentication Failures (contexto)** · `T1589 Gather Victim Identity Information`

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## O que muda aqui

- **Autor, paths UNC e software interno.** Sem isso o playbook da família mente.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como testo

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## PoC mínimo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag e39991 (metadata-pdf)
```

## Campo

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

Já abri High demais em metadata em PDFs corporativos por sintoma sem efeito. Cruzei com: Monitorar menções à marca; alertas de credential stuffing; DMARC. Sem side-effect, baixo.

## Já me queimei

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

## Blue

- Detectar: Monitorar menções à marca; alertas de credential stuffing; DMARC.
- Fechar: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.

## Evidência

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

## Refs

- [MITRE ATT&CK T1589](https://attack.mitre.org/techniques/T1589/)
- [OSINT Framework](https://osintframework.com/)
- [NIST SP 800-63](https://pages.nist.gov/800-63-3/)

## Relacionadas

- [metadata em PDFs corporativos — detecção](0402-recon-osint-people-metadata-pdf--detecao.md)
- [metadata em PDFs corporativos — path](0782-recon-osint-people-metadata-pdf--path.md)
- [correlação com breaches corporativos](0027-recon-osint-people-breach-corp.md)
- [vazamento de calendários/ICS](0025-recon-osint-people-calendar-leak.md)
- [inferência de formato de e-mail](0026-recon-osint-people-email-format.md)
- [GitHub dorking autorizado](0021-recon-osint-people-github-dorks.md)