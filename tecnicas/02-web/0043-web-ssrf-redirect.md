---
id: "0043"
categoria: "02-web"
familia: "web-ssrf"
slug: "redirect"
angulo: "base"
mitre: "T1090"
owasp: ""
tags: ["02-web", "web-ssrf", "base", "t1090"]
aliases: ["bypass via redirect aberto", "redirect"]
---

# bypass via redirect aberto

`T1090 Proxy / T1552 Unsecured Credentials (metadata)`

## Por que importa

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Variante

- **Allowlist falha se segue 302** — muda ruído e o que entra no PDF.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Passo a passo

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Exemplo

```http
POST /hook/preview HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"target":"http://internal-admin.lab.local:8443/health"}
# SSRF redirect: corpo/timing prova alcance interno — tag 57e794
```

## Nota de operador

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Armadilha

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

Já abri High demais em bypass via redirect aberto por sintoma sem efeito. Cruzei com: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254. Sem side-effect, baixo.

## Depois

Detecção — Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

Remediação — Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.

No PDF — DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

## Refs

- [MITRE ATT&CK T1090](https://attack.mitre.org/techniques/T1090/)
- [MITRE ATT&CK T1552](https://attack.mitre.org/techniques/T1552/)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [PortSwigger — SSRF](https://portswigger.net/web-security/ssrf)
- [AWS — IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

## Relacionadas

- [bypass via redirect aberto — detecção](0423-web-ssrf-redirect--detecao.md)
- [bypass via redirect aberto — path](0803-web-ssrf-redirect--path.md)
- [SSRF até o IMDS (role cloud)](0041-web-ssrf-imds.md)
- [SSRF cego com out-of-band](0042-web-ssrf-blind.md)
- [SSRF com DNS rebinding](0044-web-ssrf-dns-rebind.md)