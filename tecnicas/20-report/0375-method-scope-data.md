---
id: "0375"
categoria: "20-report"
familia: "method-scope"
slug: "data"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "base"]
aliases: ["manejo de PII/LGPD", "data"]
---

# manejo de PII/LGPD

**Methodology** · `N/A`

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## O que muda aqui

- Variante manejo de PII/LGPD: trato separado da família `method-scope`.

## Como testo

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## PoC mínimo

```text
finding_id: F-cd7d5e
variant: data
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto ORD-7781; reteste path anexado
cvss: environmental justificado (não só base)
```

## Campo

Finding sem reteste path e cleanup vira pingue-pongue.

manejo de PII/LGPD: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: N/A.

## Já me queimei

Nunca assuma que bug bounty = carte blanche.

## Blue

- Detectar: N/A
- Fechar: Processo de scoping; legal review; NDAs.

## Evidência

Template de ROE; lista de contatos; change log de escopo.

## Refs

- [PTES](http://www.pentest-standard.org/)
- [CREST guides](https://www.crest-approved.org/)
- [PTES Pre-engagement](http://www.pentest-standard.org/index.php/Pre-engagement)

## Relacionadas

- [manejo de PII/LGPD — path](0755-method-scope-data--path.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [política de stress/DoS](0372-method-scope-ddos.md)
- [stop-and-call criteria](0376-method-scope-emergency.md)