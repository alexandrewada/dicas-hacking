# CVSS 3.1 scoring disciplinado

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Detalhe

- Detalhe que pago pra ver: **Exemplos de vetores**.

## Execução

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Sinal / query

```text
finding_id: F-72235b
variant: cvss31
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
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