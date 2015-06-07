# enumeração via diretórios PGP

**A07 Identification and Authentication Failures (contexto)** · `T1589 Gather Victim Identity Information`

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## O que muda aqui

- **E-mails históricos ainda úteis** — muda ruído e o que entra no PDF.

## Como testo

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 63ddf3 (pgp-enum)
```

## Campo

CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.

Já abri High demais em enumeração via diretórios PGP por sintoma sem efeito. Cruzei com: Monitorar menções à marca; alertas de credential stuffing; DMARC. Sem side-effect, baixo.

## Já me queimei

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

## Blue

- Detectar: Monitorar menções à marca; alertas de credential stuffing; DMARC.
- Fechar: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.

## Evidência

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

## Refs

- OSINT Framework
- MITRE T1589
- NIST SP 800-63