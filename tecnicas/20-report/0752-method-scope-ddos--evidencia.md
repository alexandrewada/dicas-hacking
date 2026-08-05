---
id: "0752"
categoria: "20-report"
familia: "method-scope"
slug: "ddos"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "evidencia"]
aliases: ["política de stress/DoS", "ddos", "ddos-evidencia"]
---

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

- [PTES](http://www.pentest-standard.org/)
- [CREST guides](https://www.crest-approved.org/)
- [PTES Pre-engagement](http://www.pentest-standard.org/index.php/Pre-engagement)

## Relacionadas

- [política de stress/DoS](0372-method-scope-ddos.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [manejo de PII/LGPD](0375-method-scope-data.md)
- [stop-and-call criteria](0376-method-scope-emergency.md)