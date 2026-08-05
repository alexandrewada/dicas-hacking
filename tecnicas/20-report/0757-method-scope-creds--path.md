---
id: "0757"
categoria: "20-report"
familia: "method-scope"
slug: "creds"
angulo: "path"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "path"]
aliases: ["credenciais fornecidas vs discovered", "creds", "creds-path"]
---

# credenciais fornecidas vs discovered — path

credenciais fornecidas vs discovered como pivô. Path curto > monte de finding isolado.

## Papel

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Por que pivota

- Variante credenciais fornecidas vs discovered: trato separado da família `method-scope`.

## Cadeia

1. Entrada (escopo)
2. Pivô: credenciais fornecidas vs discovered
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Exemplo

```text
finding_id: F-4fa69a
variant: creds
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
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

- [PTES](http://www.pentest-standard.org/)
- [CREST guides](https://www.crest-approved.org/)
- [PTES Pre-engagement](http://www.pentest-standard.org/index.php/Pre-engagement)

## Relacionadas

- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [manejo de PII/LGPD](0375-method-scope-data.md)
- [política de stress/DoS](0372-method-scope-ddos.md)
- [stop-and-call criteria](0376-method-scope-emergency.md)