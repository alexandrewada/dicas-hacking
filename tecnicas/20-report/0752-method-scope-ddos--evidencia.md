# política de stress/DoS — evidência

Pacote pra política de stress/DoS sobreviver peer review.

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## O que precisa aparecer

- Variante política de stress/DoS: trato separado da família `method-scope`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Template de ROE; lista de contatos; change log de escopo.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: cf8a1c

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-ddos"}
# capturado como USER_B
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