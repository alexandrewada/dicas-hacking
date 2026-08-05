---
id: "0922"
categoria: "06-client"
familia: "client-csrf"
slug: "samesite"
angulo: "hardening"
mitre: "T1185"
owasp: ""
tags: ["06-client", "client-csrf", "hardening", "t1185"]
aliases: ["SameSite=None sem Secure", "samesite", "samesite-hardening"]
---

# SameSite=None sem Secure — hardening

Do PoC ao controle — SameSite=None sem Secure.

## Risco

CSRF força o browser autenticado a emitir requests state-changing.
Defesas (tokens, SameSite, Origin) falham por misconfig, method override, JSON com content-types
permissivos e XSS que lê tokens. SameSite=Lax não cobre tudo (chrome changes, subdomain XSS).

## Controles desta variante

- **Quebra defesa.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.

## Camadas

Hotfix: quebra a exploração direta de SameSite=None sem Secure.
Detectivo: Origin failures; CSRF token mismatch metrics.
Estrutural: Anti-CSRF tokens; SameSite=Strict/Lax consciente; Preferir Authorization header;
re-auth para ações críticas.

## No lab ficou assim

```bash
# verificação pós-hardening samesite
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/samesite/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 6305ee
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

- [SameSite=None sem Secure](0162-client-csrf-samesite.md)
- [SameSite=None sem Secure — lab](0542-client-csrf-samesite--lab.md)
- [clickjacking + CSRF](0170-client-csrf-clickjacking.md)
- [CORS reflection + CSRF](0169-client-csrf-cors.md)
- [JSON CSRF via text/plain](0163-client-csrf-json-csrf.md)
- [logout CSRF](0168-client-csrf-logout.md)