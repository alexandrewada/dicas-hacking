# SSRF até o IMDS (role cloud)

**A10:2021 SSRF** · `T1090 Proxy / T1552 Unsecured Credentials (metadata)`

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Como eu faço

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Sinal / query

```http
POST /export/fetch HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"}
# lab: resposta com role name = prova de SSRF→IMDS (sem exfiltrar secret)
# tag b6ef4c
```

## Diferencial desta nota

- **Critical em cloud; prefiro provar com token/role name redigido** — muda ruído e o que entra no PDF.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

Já abri High demais em roubo de role via IMDS por sintoma sem efeito. Cruzei com: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254. Sem side-effect, baixo.

## Onde já errei

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Entrega

- blue: Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.
- fix: Allowlist de destinos; bloquear link-local; IMDSv2; network policies;
parse URL com lib única e canônica.
- proof: DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

## Refs

- OWASP SSRF
- PortSwigger SSRF
- AWS IMDSv2