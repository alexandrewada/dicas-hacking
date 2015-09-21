# GitHub dorking autorizado — detecção

Purple em GitHub dorking autorizado: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Hipótese

- **Busque secrets da org no escopo; trate vazamento como Critical.** Sem isso o playbook da família mente.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1589 Gather Victim Identity Information`.

### PoC

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## Sinal / query

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — github-dorks 796636
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

- OSINT Framework
- MITRE T1589
- NIST SP 800-63