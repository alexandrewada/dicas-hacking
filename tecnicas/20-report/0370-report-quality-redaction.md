# como publicar amostra sem vazar cliente

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## Detalhe

- Variante como publicar amostra sem vazar cliente: trato separado da família `report-quality`.

## Execução

1. Separar evidência técnica de narrativa de negócio.
2. Passos numerados com dados de teste.
3. CVSS vector explícito.
4. Remediação short/long term.
5. Apêndice com IOCs e cleanup.

## Exemplo

```text
finding_id: F-c78dc6
variant: redaction
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
cvss: environmental justificado (não só base)
```

## OpSec

CVSS é input. Justifico environmental e impacto real do cliente.

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