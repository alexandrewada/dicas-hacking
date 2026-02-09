# apêndice técnico vs executivo

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Detalhe

- Variante apêndice técnico vs executivo: trato separado da família `report-quality`.

## Execução

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## PoC mínimo

```text
finding_id: F-6bf602
variant: appendix
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## OpSec

Não inclua dados reais de clientes em material público — redija.

## Cuidados

Não inclua dados reais de clientes em material público — redija.

## Fechamento

| | |
|---|---|
| Detecção | N/A |
| Remediação | Templates de relatório; peer review; threat model alinhado. |
| Evidência | Exemplo de finding redigido; CVSS; remediação. |

## Refs

- PTES
- OSSTMM
- CVSS