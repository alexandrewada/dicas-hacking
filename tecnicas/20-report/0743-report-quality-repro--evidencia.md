# passos de reprodução perfeitos — evidência

Pacote pra passos de reprodução perfeitos sobreviver peer review.

## Contexto

Um finding forte tem: título preciso, risco de negócio, passos reproduzíveis,
evidência, impacto CVSS 3.1/4.0 justificado e remediação acionável por squad.
Evito inflar CVSS e jargão vazio.

## O que precisa aparecer

- Variante passos de reprodução perfeitos: trato separado da família `report-quality`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Exemplo de finding redigido; CVSS; remediação.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: ef4c24

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-repro"}
# capturado como USER_B
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