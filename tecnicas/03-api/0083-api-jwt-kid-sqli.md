---
id: "0083"
categoria: "03-api"
familia: "api-jwt"
slug: "kid-sqli"
angulo: "base"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "base", "t1550"]
aliases: ["JWT kid injection", "kid-sqli"]
---

# JWT kid injection

**A07 Identification and Authentication Failures** · `T1550 Use Alternate Authentication Material`

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## O que muda aqui

- **Quando kid vai ao DB/FS** — muda ruído e o que entra no PDF.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Como testo

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_kid-sqli_5b6379
# claim tamper / kid / aud — ver variante kid-sqli
```

## Campo

403 no gateway com 200 no origin — path direto e Host conforme ROE.

Antes de Critical em kid SQL/path injection, confiro se a telemetria que eu cobraria reagiria — Invalid signature spikes; impossible travel com tokens; denylist.

## Já me queimei

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## Blue

- Detectar: Invalid signature spikes; impossible travel com tokens; denylist.
- Fechar: Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

## Evidência

Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)

## Relacionadas

- [JWT kid injection — detecção](0463-api-jwt-kid-sqli--detecao.md)
- [JWT kid injection — path](0843-api-jwt-kid-sqli--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)