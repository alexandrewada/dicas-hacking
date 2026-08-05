---
id: "0750"
categoria: "20-report"
familia: "report-quality"
slug: "redaction"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "evidencia"]
aliases: ["como publicar amostra sem vazar cliente", "redaction", "redaction-evidencia"]
---

# como publicar amostra sem vazar cliente — evidência

Pacote pra como publicar amostra sem vazar cliente sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Variante como publicar amostra sem vazar cliente: trato separado da família `report-quality`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/obj_e02541 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (redaction)
hash_prova: e02541
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

- [como publicar amostra sem vazar cliente](0370-report-quality-redaction.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)