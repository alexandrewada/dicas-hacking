# ROE de verdade

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

## No lab ficou assim

```text
finding_id: F-972b39
variant: roe-template
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto a1b2c3d4-e5f6-7890-abcd-ef1234567890; reteste path anexado
cvss: environmental justificado (não só base)
```

## Diferencial desta nota

- Variante template de Rules of Engagement: trato separado da família `method-scope`.

Antes de Critical em template de Rules of Engagement, confiro se a telemetria que eu cobraria reagiria — N/A.

## Onde já errei

Nunca assuma que bug bounty = carte blanche.

Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.

## Entrega

- blue: N/A
- fix: Processo de scoping; legal review; NDAs.
- proof: Template de ROE; lista de contatos; change log de escopo.

## Refs

- PTES Pre-engagement
- CREST guides