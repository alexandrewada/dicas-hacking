---
id: "0084"
categoria: "03-api"
familia: "api-jwt"
slug: "jku"
angulo: "base"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "base", "t1550"]
aliases: ["jku/x5u SSRF + key inject", "jku"]
---

# jku/x5u SSRF + key inject

`T1550 Use Alternate Authentication Material`

## Por que importa

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Variante

- Detalhe que pago pra ver: **Hospede JWKS só se ROE permitir**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Passo a passo

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## PoC mínimo

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_jku_bd8269
# claim tamper / kid / aud — ver variante jku
```

## Nota de operador

Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.

## Armadilha

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

Falso amigo em jku/x5u SSRF + key inject: UI/log gritam, impacto não. Exijo Invalid signature spikes.

## Depois

Detecção — Invalid signature spikes; impossible travel com tokens; denylist.

Remediação — Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

No PDF — Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)

## Relacionadas

- [jku/x5u SSRF + key inject — detecção](0464-api-jwt-jku--detecao.md)
- [jku/x5u SSRF + key inject — path](0844-api-jwt-jku--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)