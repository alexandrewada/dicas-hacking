# stop-and-call criteria

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Detalhe

- Variante stop-and-call criteria: trato separado da família `method-scope`.

## Execução

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Sinal / query

```text
finding_id: F-12605b
variant: emergency
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## OpSec

Nunca assuma que bug bounty = carte blanche.

## Cuidados

Nunca assuma que bug bounty = carte blanche.

## Fechamento

| | |
|---|---|
| Detecção | N/A |
| Remediação | Processo de scoping; legal review; NDAs. |
| Evidência | Template de ROE; lista de contatos; change log de escopo. |

## Refs

- PTES Pre-engagement
- CREST guides