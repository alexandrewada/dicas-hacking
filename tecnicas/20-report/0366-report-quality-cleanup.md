---
id: "0366"
categoria: "20-report"
familia: "report-quality"
slug: "cleanup"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "report-quality", "base"]
aliases: ["cleanup & artifact list", "cleanup"]
---

# cleanup & artifact list

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

## Exemplo

```text
finding_id: F-82b6be
variant: cleanup
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
cvss: environmental justificado (não só base)
```

## Diferencial desta nota

- Variante cleanup & artifact list: trato separado da família `report-quality`.

Antes de Critical em cleanup & artifact list, confiro se a telemetria que eu cobraria reagiria — N/A.

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

- [cleanup & artifact list — evidência](0746-report-quality-cleanup--evidencia.md)
- [apêndice técnico vs executivo](0369-report-quality-appendix.md)
- [narrativa de account takeover](0367-report-quality-ato.md)
- [Traduzir risco pro CISO](0364-report-quality-business.md)
- [findings encadeados](0368-report-quality-chain.md)