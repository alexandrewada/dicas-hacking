---
id: "0362"
categoria: "20-report"
familia: "report-quality"
slug: "cvss40"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "base"]
aliases: ["CVSS 4.0 essentials", "cvss40"]
---

# CVSS 4.0 essentials

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Detalhe

- Variante CVSS 4.0 essentials: trato separado da família `report-quality`.

## Execução

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Exemplo

```text
finding_id: F-92ded7
variant: cvss40
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## OpSec

Não inclua dados reais de clientes em material público — redija. Finding sem reteste path e cleanup vira pingue-pongue.

## Cuidados

Não inclua dados reais de clientes em material público — redija.

## Fechamento

| | |
|---|---|
| Detecção | N/A |
| Remediação | Templates de relatório; peer review; threat model alinhado. |
| Evidência | Exemplo de finding redigido; CVSS; remediação. |

## Refs

- [PTES](http://www.pentest-standard.org/)
- [OSSTMM](https://www.isecom.org/research.html)
- [FIRST — CVSS](https://www.first.org/cvss/)

## Relacionadas

- [CVSS 4.0 essentials — evidência](0742-report-quality-cvss40--evidencia.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)