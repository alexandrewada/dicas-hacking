---
id: "0921"
categoria: "06-client"
familia: "client-csrf"
slug: "token-missing"
angulo: "hardening"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "hardening", "t1185"]
aliases: ["ausência total de token", "token-missing", "token-missing-hardening"]
---

# ausência total de token — hardening

Do PoC ao controle — ausência total de token.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Finding clássico.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

Controle que fecha: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Sinal que deveria existir: Origin failures; CSRF token mismatch metrics.

## No lab ficou assim

```text
antes: controle ausente para token-missing
depois: ownership check / deny default em TARGET
verificação: PoC fa73c8 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Login CSRF também importa. Não executo ações em contas alheias.

## Antes/depois

PoC HTML; request forjado; efeito na conta teste.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1185](https://attack.mitre.org/techniques/T1185/)
- [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — CSRF](https://portswigger.net/web-security/csrf)

## Relacionadas

- [ausência total de token](0161-client-csrf-token-missing.md)
- [ausência total de token — lab](0541-client-csrf-token-missing--lab.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [isAdmin/role elevation (path)](../03-api/0061-api-mass-assignment-role-flag.md)