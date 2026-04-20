# ROE de verdade — evidência

Pacote pra ROE de verdade sobreviver peer review.

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## O que precisa aparecer

- Variante template de Rules of Engagement: trato separado da família `method-scope`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Template de ROE; lista de contatos; change log de escopo.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (roe-template)
hash_prova: 787746
```

## Remediação junto

Processo de scoping; legal review; NDAs.

## Se purple

N/A

## Armadilha

Nunca assuma que bug bounty = carte blanche.

## Refs

- PTES Pre-engagement
- CREST guides