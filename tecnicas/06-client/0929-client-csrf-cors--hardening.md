---
id: "0929"
categoria: "06-client"
familia: "client-csrf"
slug: "cors"
angulo: "hardening"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "hardening", "t1185"]
aliases: ["CORS reflection + CSRF", "cors", "cors-hardening"]
---

# CORS reflection + CSRF — hardening

Do PoC ao controle — CORS reflection + CSRF.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- Se não validar **Amplifica impacto**, a nota fica genérica.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.
- Origin refletido + credentials. Read autenticado de origem atacante — não só ACAO *.

## Camadas

Controle que fecha: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.
Sinal que deveria existir: Origin failures; CSRF token mismatch metrics.

## PoC mínimo

```text
antes: controle ausente para cors
depois: ownership check / deny default em TARGET
verificação: PoC 0290a3 retorna 403/blocked
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

- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [CORS reflection + CSRF — lab](0549-client-csrf-cors--lab.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)
- [X-HTTP-Method-Override](0164-client-csrf-method-override.md)