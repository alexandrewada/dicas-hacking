# apêndice técnico vs executivo — evidência

Pacote pra apêndice técnico vs executivo sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Variante apêndice técnico vs executivo: trato separado da família `report-quality`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (appendix)
hash_prova: 089622
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