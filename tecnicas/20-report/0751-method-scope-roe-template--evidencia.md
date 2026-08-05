---
id: "0751"
categoria: "20-report"
familia: "method-scope"
slug: "roe-template"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "evidencia"]
aliases: ["ROE de verdade", "roe-template", "roe-template-evidencia"]
---

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

- [PTES](http://www.pentest-standard.org/)
- [CREST guides](https://www.crest-approved.org/)
- [PTES Pre-engagement](http://www.pentest-standard.org/index.php/Pre-engagement)

## Relacionadas

- [ROE de verdade](0371-method-scope-roe-template.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [manejo de PII/LGPD](0375-method-scope-data.md)
- [política de stress/DoS](0372-method-scope-ddos.md)