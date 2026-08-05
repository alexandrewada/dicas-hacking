---
id: "0466"
categoria: "03-api"
familia: "api-jwt"
slug: "claim-tamper"
angulo: "detecao"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "detecao", "t1550"]
aliases: ["tampering de role/admin", "claim-tamper", "claim-tamper-detecao"]
---

# tampering de role/admin — detecção

Gap de detecção em `T1550 Use Alternate Authentication Material` / tampering de role/admin. PoC mínimo, telemetria ligada.

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Hipótese

- Se não validar **Sem verificação de assinatura efetiva**, a nota fica genérica.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Exemplo

```text
authz_fail OR jwt_verify_error claim=claim-tamper
alerta se alg in (none, HS256) com key pública — tag b64639
```

## Sinal

Invalid signature spikes; impossible travel com tokens; denylist.

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.

## Evidência

Token de teste manipulado; response privilegiada; libs/versão.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_Cheat_Sheet.html)

## Relacionadas

- [tampering de role/admin](0086-api-jwt-claim-tamper.md)
- [tampering de role/admin — path](0846-api-jwt-claim-tamper--path.md)
- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)