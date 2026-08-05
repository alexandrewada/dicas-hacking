---
id: "0367"
categoria: "20-report"
familia: "report-quality"
slug: "ato"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "base"]
aliases: ["narrativa de account takeover", "ato"]
---

# narrativa de account takeover

**Methodology** · `N/A`

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que muda aqui

- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

## Como testo

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Sinal / query

```text
finding_id: F-0cf279
variant: ato
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto obj_0cf279; reteste path anexado
cvss: environmental justificado (não só base)
```

## Campo

Finding sem reteste path e cleanup vira pingue-pongue.

Falso amigo em narrativa de account takeover: UI/log gritam, impacto não. Exijo N/A.

## Já me queimei

Não inclua dados reais de clientes em material público — redija.

## Blue

- Detectar: N/A
- Fechar: Templates de relatório; peer review; threat model alinhado.

## Evidência

Exemplo de finding redigido; CVSS; remediação.

## Refs

- [PTES](http://www.pentest-standard.org/)
- [OSSTMM](https://www.isecom.org/research.html)
- [FIRST — CVSS](https://www.first.org/cvss/)

## Relacionadas

- [narrativa de account takeover — evidência](0747-report-quality-ato--evidencia.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)
- [cleanup & artifact list](0366-report-quality-cleanup.md)