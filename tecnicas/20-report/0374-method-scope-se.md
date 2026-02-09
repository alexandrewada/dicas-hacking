# scoping social engineering

**Methodology** · `N/A`

Engajamentos falham por escopo ambíguo. negociam: in/out of scope,
dados sensíveis, DoS rules, SE rules, cloud accounts, emergency contacts e evidência.
Isso diferencia amador de profissional.

**Variante:** Variante scoping social engineering: trato separado da família `method-scope`.

**Método**

1. Checklist de ROE antes do kickoff.
2. Inventário de ativos confirmado.
3. Canais de emergência.
4. Regras de exfil e storage de evidência.
5. Kickoff com blue team se purple.

## Exemplo

```text
finding_id: F-b74708
variant: se
repro: passos 1–n em lab.local com USER_A
cleanup: reverter objeto obj_b74708; reteste path anexado
cvss: environmental justificado (não só base)
```

**Freio:** Nunca assuma que bug bounty = carte blanche.

Antes de Critical em scoping social engineering, confiro se a telemetria que eu cobraria reagiria — N/A.

Detecto via: N/A

Corrijo com: Processo de scoping; legal review; NDAs.

Levo no report: Template de ROE; lista de contatos; change log de escopo.

Refs: PTES Pre-engagement, CREST guides