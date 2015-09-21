# pretext a partir de LinkedIn — detecção

Gap de detecção em `T1589 Gather Victim Identity Information` / pretext a partir de LinkedIn. PoC mínimo, telemetria ligada.

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Hipótese

- **Somente se SE estiver no ROE** — muda ruído e o que entra no PDF.

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
DNS NXDOMAIN spike for enum pattern — linkedin-pretext 871e0e
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

- OSINT Framework
- MITRE T1589
- NIST SP 800-63