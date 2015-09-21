# inferência de formato de e-mail — path

inferência de formato de e-mail como pivô. Path curto > monte de finding isolado.

## Papel

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Por que pivota

- Se não validar **Valide com cuidado para não spammar**, a nota fica genérica.

## Cadeia

1. Entrada (escopo)
2. Pivô: inferência de formato de e-mail
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
# marcar dev-/staging- ; tag 352b91 (email-format)
```

## Freio

Não compre/abuse dados ilegais. Não contacte pessoas fora do ROE.
LGPD: minimize PII no relatório.

## No caminho

Detectar: Monitorar menções à marca; alertas de credential stuffing; DMARC.

Remediar: Treinamento contínuo; passwordless/FIDO2; rate-limit de auth; canary accounts.

## Prova

Lista de identidades com fonte; **sem** senhas em claro no relatório se evitável.

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Refs

- OSINT Framework
- MITRE T1589
- NIST SP 800-63