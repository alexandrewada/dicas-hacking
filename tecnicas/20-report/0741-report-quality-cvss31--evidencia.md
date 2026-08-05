---
id: "0741"
categoria: "20-report"
familia: "report-quality"
slug: "cvss31"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "evidencia"]
aliases: ["CVSS 3.1 scoring disciplinado", "cvss31", "cvss31-evidencia"]
---

# CVSS 3.1 scoring disciplinado — evidência

Pacote pra CVSS 3.1 scoring disciplinado sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Detalhe que pago pra ver: **Exemplos de vetores**.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/obj_63cf6a Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (cvss31)
hash_prova: 63cf6a
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

- [CVSS 3.1 scoring disciplinado](0361-report-quality-cvss31.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)