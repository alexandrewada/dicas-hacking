---
id: "0380"
categoria: "20-report"
familia: "method-scope"
slug: "kickoff"
angulo: "base"
mitre: ""
owasp: ""
tags: ["20-report", "method-scope", "base"]
aliases: ["agenda de kickoff técnica", "kickoff"]
---

# agenda de kickoff técnica

**Methodology** · `N/A`

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## O que muda aqui

- Variante agenda de kickoff técnica: trato separado da família `method-scope`.

## Como testo

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Exemplo

```text
finding_id: F-880b99
variant: kickoff
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto ORD-7781; reteste path anexado
cvss: environmental justificado (não só base)
```

## Campo

Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.

agenda de kickoff técnica: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: N/A.

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

- [agenda de kickoff técnica — path](0760-method-scope-kickoff--path.md)
- [scoping multi-cloud](0373-method-scope-cloud.md)
- [credenciais fornecidas vs discovered](0377-method-scope-creds.md)
- [manejo de PII/LGPD](0375-method-scope-data.md)
- [política de stress/DoS](0372-method-scope-ddos.md)