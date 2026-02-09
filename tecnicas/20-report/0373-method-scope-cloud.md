# scoping multi-cloud

`N/A`

## Por que importa

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Variante

- Variante scoping multi-cloud: trato separado da família `method-scope`.

## Passo a passo

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## PoC mínimo

```text
finding_id: F-93290a
variant: cloud
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto usr_01HZX; reteste path anexado
cvss: environmental justificado (não só base)
```

## Nota de operador

Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.

## Armadilha

Nunca assuma que bug bounty = carte blanche.

scoping multi-cloud: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: N/A.

## Depois

Detecção — N/A

Remediação — Processo de scoping; legal review; NDAs.

No PDF — Template de ROE; lista de contatos; change log de escopo.

## Refs

- PTES Pre-engagement
- CREST guides