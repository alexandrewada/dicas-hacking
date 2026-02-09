# ativos de terceiros

`N/A`

## Por que importa

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Variante

- Detalhe que pago pra ver: **SaaS boundaries**.

## Passo a passo

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## No lab ficou assim

```text
finding_id: F-29856d
variant: third-party
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto obj_29856d; reteste path anexado
cvss: environmental justificado (não só base)
```

## Nota de operador

Finding sem reteste path e cleanup vira pingue-pongue.

## Armadilha

Nunca assuma que bug bounty = carte blanche.

Antes de Critical em ativos de terceiros, confiro se a telemetria que eu cobraria reagiria — N/A.

## Depois

Detecção — N/A

Remediação — Processo de scoping; legal review; NDAs.

No PDF — Template de ROE; lista de contatos; change log de escopo.

## Refs

- PTES Pre-engagement
- CREST guides