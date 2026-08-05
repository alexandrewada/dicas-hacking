---
id: "0364"
categoria: "20-report"
familia: "report-quality"
slug: "business"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "base"]
aliases: ["Traduzir risco pro CISO", "business"]
---

# Traduzir risco pro CISO

**Methodology** · `N/A`

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Como eu faço

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## No lab ficou assim

```text
finding_id: F-e46767
variant: business
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## Diferencial desta nota

- Variante traduzir risco para CISO: trato separado da família `report-quality`.

traduzir risco para CISO: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: N/A.

## Onde já errei

Não inclua dados reais de clientes em material público — redija.

CVSS é input. Justifico environmental e impacto real do cliente.

## Entrega

- blue: N/A
- fix: Templates de relatório; peer review; threat model alinhado.
- proof: Exemplo de finding redigido; CVSS; remediação.

## Refs

- [PTES](http://www.pentest-standard.org/)
- [OSSTMM](https://www.isecom.org/research.html)
- [FIRST — CVSS](https://www.first.org/cvss/)

## Relacionadas

- [Traduzir risco pro CISO — evidência](0744-report-quality-business--evidencia.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [findings encadeados](0368-report-quality-chain.md)
- [cleanup & artifact list](0366-report-quality-cleanup.md)