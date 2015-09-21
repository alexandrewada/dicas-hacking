# inferência de formato de e-mail — detecção

Se o SOC não vê inferência de formato de e-mail, o finding é de cobertura, não de ego ofensivo.

## Contexto

Phishing e password spraying bem-sucedidos começam com higiene OSINT:
e-mails, cargos, tech stack de vagas, vazamentos e padrões de senha corporativa.
Em pentest com ROE de social engineering, isso fundamenta pretexts realistas e éticos.

## Hipótese

- Se não validar **Valide com cuidado para não spammar**, a nota fica genérica.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Coleto e-mails públicos (site, GitHub, PDF metadata) no escopo.
2. Normalizar formatos (flast, first.last) e validar só se permitido.
3. Cruzar com breaches públicos (haveibeenpwned API / datasets autorizados).
4. Extrair tech de job posts para priorizar vetores.
5. Monto matriz de alvos de phishing **aprovados** pelo cliente.

## Exemplo

```text
CT monitor: new SAN *.lab.local issued
DNS NXDOMAIN spike for enum pattern — email-format 77dceb
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