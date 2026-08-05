---
id: "0082"
categoria: "03-api"
familia: "api-jwt"
slug: "rs-hs"
angulo: "base"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "base", "t1550"]
aliases: ["Confusão RS256/HS256", "rs-hs"]
---

# Confusão RS256/HS256

## Leitura rápida

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Foco

- **Secret = public key.** Sem isso o playbook da família mente.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Mãos na massa

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```http
GET /api/v1/admin/users HTTP/1.1
Host: api.lab.local
Authorization: Bearer JWT_rs-hs_94f25e
# claim tamper / kid / aud — ver variante rs-hs
```

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

## Pitfall

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

## Detecção / remediação

Invalid signature spikes; impossible travel com tokens; denylist.

→ Bibliotecas atualizadas; enforce algorithm; short TTL + refresh rotation;
bind token a client quando possível; revogação.

## Prova

Token de teste manipulado; response privilegiada; libs/versão.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [Confusão RS256/HS256 — detecção](0462-api-jwt-rs-hs--detecao.md)
- [Confusão RS256/HS256 — path](0842-api-jwt-rs-hs--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)
- [jku/x5u SSRF + key inject (path)](0084-api-jwt-jku.md)