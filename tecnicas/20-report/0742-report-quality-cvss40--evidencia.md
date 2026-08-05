---
id: "0742"
categoria: "20-report"
familia: "report-quality"
slug: "cvss40"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "evidencia"]
aliases: ["CVSS 4.0 essentials", "cvss40", "cvss40-evidencia"]
---

# CVSS 4.0 essentials — evidência

Pacote pra CVSS 4.0 essentials sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Variante CVSS 4.0 essentials: trato separado da família `report-quality`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (cvss40)
hash_prova: e51b74
```

## Remediação junto

Templates de relatório; peer review; threat model alinhado.

## Se purple

N/A

## Armadilha

Não inclua dados reais de clientes em material público — redija.

## Refs

- [PTES](http://www.pentest-standard.org/)
- [OSSTMM](https://www.isecom.org/research.html)
- [FIRST — CVSS](https://www.first.org/cvss/)

## Relacionadas

- [CVSS 4.0 essentials](0362-report-quality-cvss40.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)