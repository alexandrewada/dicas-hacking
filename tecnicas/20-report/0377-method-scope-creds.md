# credenciais fornecidas vs discovered

**Methodology** · `N/A`

## Contexto

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

## Como eu faço

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Sinal / query

```text
finding_id: F-318678
variant: creds
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto 10042; reteste path anexado
cvss: environmental justificado (não só base)
```

## Diferencial desta nota

- Variante credenciais fornecidas vs discovered: trato separado da família `method-scope`.

Antes de Critical em credenciais fornecidas vs discovered, confiro se a telemetria que eu cobraria reagiria — N/A.

## Onde já errei

Nunca assuma que bug bounty = carte blanche.

Finding sem reteste path e cleanup vira pingue-pongue.

## Entrega

- blue: N/A
- fix: Processo de scoping; legal review; NDAs.
- proof: Template de ROE; lista de contatos; change log de escopo.

## Refs

- PTES Pre-engagement
- CREST guides