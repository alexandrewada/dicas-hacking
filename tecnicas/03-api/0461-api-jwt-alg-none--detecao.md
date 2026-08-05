---
id: "0461"
categoria: "03-api"
familia: "api-jwt"
slug: "alg-none"
angulo: "detecao"
mitre: "T1550"
owasp: ""
tags: ["03-api", "api-jwt", "detecao", "t1550"]
aliases: ["JWT com alg=none", "alg-none", "alg-none-detecao"]
---

# JWT com alg=none — detecção

Purple em JWT com alg=none: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

JWTs mal implementados permitem alg=none, confusão RS256/HS256, kid injection (SQL/path),
claims sensíveis sem validação de iss/aud/exp, e tokens eternamente válidos sem revogação.
Valido a biblioteca verificadora, não só o conteúdo do token.

## Hipótese

- **Classic; ainda aparece em libs custom.** Sem isso o playbook da família mente.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1550 Use Alternate Authentication Material`.

### PoC

1. Decodifico header/payload; mapeio claims.
2. Testo alg none e troca de algoritmo conforme biblioteca.
3. Avalio kid/jku/x5u se presentes (SSRF/file).
4. Verifico aud/iss/nbf/exp e clock skew.
5. Testo privilege claims e token sidejacking.

## Sinal / query

```kusto
AppTraces
| where Message has 'jwt' and Message has 'alg'
| where Message has 'none' or Message has 'verify failed'
| project TimeGenerated, Message
// jwt alg-none 070f8b
```

## Sinal

Invalid signature spikes; impossible travel com tokens; denylist.

## Freio

Nem todo JWT 'sem exp' é explorável se houver store server-side.
Não exfiltro tokens de usuários reais — uso contas de teste.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Evidência

Token de teste manipulado; response privilegiada; libs/versão.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1550](https://attack.mitre.org/techniques/T1550/)
- [RFC 7519 — JWT](https://www.rfc-editor.org/rfc/rfc7519)
- [PortSwigger — JWT attacks](https://portswigger.net/web-security/jwt)
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)

## Relacionadas

- [JWT com alg=none](0081-api-jwt-alg-none.md)
- [JWT com alg=none — path](0841-api-jwt-alg-none--path.md)
- [Confusão RS256/HS256](0082-api-jwt-rs-hs.md)
- [tampering de role/admin](0086-api-jwt-claim-tamper.md)
- [isAdmin/role elevation (path)](0061-api-mass-assignment-role-flag.md)
- [scope elevation (path)](../04-auth/0118-auth-oauth-oidc-scope-escalation.md)