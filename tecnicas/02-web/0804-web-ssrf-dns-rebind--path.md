---
id: "0804"
categoria: "02-web"
familia: "web-ssrf"
slug: "dns-rebind"
angulo: "path"
mitre: ""
owasp: ""
tags: ["02-web", "web-ssrf", "path"]
aliases: ["SSRF com DNS rebinding", "dns-rebind", "dns-rebind-path"]
---

# SSRF com DNS rebinding — path

SSRF com DNS rebinding como pivô. Path curto > monte de finding isolado.

## Papel

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Por que pivota

- **TTL baixo para burlar checagem toctou** — muda ruído e o que entra no PDF.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Cadeia

1. Entrada (escopo)
2. Pivô: SSRF com DNS rebinding
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## PoC mínimo

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8080/health"}
# SSRF dns-rebind: corpo/timing prova alcance interno — tag bd304c
```

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

## No caminho

Detectar: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

Remediar: Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

## Prova

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Refs

- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)
- [SSRF com DNS rebinding — detecção](0424-web-ssrf-dns-rebind--detecao.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)