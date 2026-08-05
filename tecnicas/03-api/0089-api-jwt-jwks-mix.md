---
id: "0089"
categoria: "03-api"
familia: "api-jwt"
slug: "jwks-mix"
angulo: "base"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "base", "t1550"]
aliases: ["JWKS key confusion multi-tenant", "jwks-mix"]
---

# JWKS key confusion multi-tenant

**A07 Identification and Authentication Failures** · `T1550 Use Alternate Authentication Material`

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

**Variante:** Se não validar **kid de outro tenant**, a nota fica genérica. Testo verify path na lib real. Claim admin:true sem verify não é bypass.

**Método**

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## No lab ficou assim

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_jwks-mix_19e49d
# claim tamper / kid / aud — ver variante jwks-mix
```

**Freio:** Nem todo JWT 'sem exp' é explorável se houver store server-side.

Falso amigo em JWKS key confusion multi-tenant: UI/log gritam, impacto não. Exijo Invalid signature spikes.

Detecto via: Invalid signature spikes; impossible travel com tokens; denylist.

Corrijo com: Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

Levo no report: Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [JWKS key confusion multi-tenant — detecção](0469-api-jwt-jwks-mix--detecao.md)
- [JWKS key confusion multi-tenant — path](0849-api-jwt-jwks-mix--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)