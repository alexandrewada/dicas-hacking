---
id: "0760"
categoria: "20-report"
familia: "method-scope"
slug: "kickoff"
angulo: "path"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "path"]
aliases: ["agenda de kickoff técnica", "kickoff", "kickoff-path"]
---

# agenda de kickoff técnica — path

agenda de kickoff técnica como pivô. Path curto > monte de finding isolado.

## Papel

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Por que pivota

- Variante agenda de kickoff técnica: trato separado da família `method-scope`.

## Cadeia

1. Entrada (escopo)
2. Pivô: agenda de kickoff técnica
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## No lab ficou assim

```text
finding_id: F-66b66b
variant: kickoff
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

- [PTES](http://www.pentest-standard.org/)
- [CREST guides](https://www.crest-approved.org/)
- [PTES Pre-engagement](http://www.pentest-standard.org/index.php/Pre-engagement)

## Relacionadas

- [agenda de kickoff técnica](0380-method-scope-kickoff.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [manejo de PII/LGPD](0375-method-scope-data.md)
- [política de stress/DoS](0372-method-scope-ddos.md)