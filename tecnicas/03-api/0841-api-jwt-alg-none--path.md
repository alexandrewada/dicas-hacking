---
id: "0841"
categoria: "03-api"
familia: "api-jwt"
slug: "alg-none"
angulo: "path"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "path", "t1550"]
aliases: ["JWT com alg=none", "alg-none", "alg-none-path"]
---

# JWT com alg=none — path

JWT com alg=none como pivô. Path curto > monte de finding isolado.

## Papel

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Por que pivota

- **Classic; ainda aparece em libs custom.** Sem isso o playbook da família mente.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Cadeia

1. Entrada (escopo)
2. Pivô: JWT com alg=none
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```http
GET /api/me HTTP/1.1
Host: api.lab.local
Authorization: Bearer eyJhbGciOiJub25lIn0.eyJzdWIiOiJUSER_AIiwicm9sZSI6ImFkbWluIn0.
# se 200 com role admin sem verify → alg=none aceito
# tag b3583b
```

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## No caminho

Detectar: Invalid signature spikes; impossible travel com tokens; denylist.

Remediar: Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

## Prova

Token de teste manipulado; response privilegiada; libs/versão.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [JWT com alg=none — detecção](0461-api-jwt-alg-none--detecao.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)
- [isAdmin/role elevation (path)](0061-api-mass-assignment-role-flag.md)
- [scope elevation (path)](../04-auth/0118-auth-oauth-oidc-scope-escalation.md)