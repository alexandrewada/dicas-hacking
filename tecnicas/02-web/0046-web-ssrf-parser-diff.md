# diferenciais de parser URL

## Leitura rápida

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Foco

- Detalhe que pago pra ver: **Go vs urllib vs browser**.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Mãos na massa

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## No lab ficou assim

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8080/health"}
# SSRF parser-diff: corpo/timing prova alcance interno — tag 0fd668
```

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Pitfall

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

## Detecção / remediação

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

→ Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

## Prova

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

## Refs

- OWASP SSRF
- PortSwigger SSRF
- AWS IMDSv2