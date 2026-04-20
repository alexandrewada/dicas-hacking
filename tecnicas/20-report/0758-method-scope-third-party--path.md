# ativos de terceiros — path

ativos de terceiros como pivô. Path curto > monte de finding isolado.

## Papel

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Por que pivota

- Detalhe que pago pra ver: **SaaS boundaries**.

## Cadeia

1. Entrada (escopo)
2. Pivô: ativos de terceiros
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Sinal / query

```text
finding_id: F-92ce51
variant: third-party
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
cvss: environmental justificado (não só base)
```

## Freio

Nunca assuma que bug bounty = carte blanche.

## No caminho

Detectar: N/A

Remediar: Processo de scoping; legal review; NDAs.

## Prova

Template de ROE; lista de contatos; change log de escopo.

Finding sem reteste path e cleanup vira pingue-pongue.

## Refs

- PTES Pre-engagement
- CREST guides