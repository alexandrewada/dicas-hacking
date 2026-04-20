# scoping multi-cloud — path

scoping multi-cloud como pivô. Path curto > monte de finding isolado.

## Papel

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Por que pivota

- Variante scoping multi-cloud: trato separado da família `method-scope`.

## Cadeia

1. Entrada (escopo)
2. Pivô: scoping multi-cloud
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
finding_id: F-d6aa01
variant: cloud
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

Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.

## Refs

- PTES Pre-engagement
- CREST guides