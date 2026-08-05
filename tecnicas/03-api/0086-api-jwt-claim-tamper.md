---
id: "0086"
categoria: "03-api"
familia: "api-jwt"
slug: "claim-tamper"
angulo: "base"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "base", "t1550"]
aliases: ["tampering de role/admin", "claim-tamper"]
---

# tampering de role/admin

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Detalhe

- Se não validar **Sem verificação de assinatura efetiva**, a nota fica genérica.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Execução

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_claim-tamper_777853
# claim tamper / kid / aud — ver variante claim-tamper
```

## OpSec

Nem todo JWT 'sem exp' é explorável se houver store server-side.

## Cuidados

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## Fechamento

| | |
|---|---|
| Detecção | Invalid signature spikes; impossible travel com tokens; denylist. |
| Remediação | Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação. |
| Evidência | Token de teste manipulado; response privilegiada; libs/versão. |

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [tampering de role/admin — detecção](0466-api-jwt-claim-tamper--detecao.md)
- [tampering de role/admin — path](0846-api-jwt-claim-tamper--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)