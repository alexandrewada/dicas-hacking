# CVSS 3.1 scoring disciplinado — evidência

Pacote pra CVSS 3.1 scoring disciplinado sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Detalhe que pago pra ver: **Exemplos de vetores**.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/obj_63cf6a Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (cvss31)
hash_prova: 63cf6a
```

## Remediação junto

Templates de relatório; peer review; threat model alinhado.

## Se purple

N/A

## Armadilha

Não inclua dados reais de clientes em material público — redija.

## Refs

- PTES
- OSSTMM
- CVSS