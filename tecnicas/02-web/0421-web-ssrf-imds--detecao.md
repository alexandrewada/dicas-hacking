# SSRF até o IMDS (role cloud) — detecção

Purple em SSRF até o IMDS (role cloud): uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

SSRF força o servidor a buscar URLs controladas pelo atacante, alcançando rede interna,
metadata cloud (169.254.169.254), e às vezes RCE via gopher/dict em serviços frágeis.
Diferencio SSRF cego vs com resposta, e bypass de allowlists (DNS rebinding,
redirect chains, URL parser differentials, IPv6/decimal IP).

## Hipótese

- **Critical em cloud; prefiro provar com token/role name redigido** — muda ruído e o que entra no PDF.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1090 Proxy / T1552 Unsecured Credentials (metadata)`.

### PoC

1. Identifico sinks: webhooks, PDF generators, importers, avatars, health checks.
2. Testo http(s) para burp collaborator / interactsh **do engajamento**.
3. Tento metadata endpoints cloud se in-scope.
4. Exploro redirects, DNS rebinding e encodings de IP.
5. Avalio protocolo wrappers apenas se ROE permitir e risco aceito.

## Sinal / query

```kusto
CloudAppEvents
| where RequestURL has '169.254.169.254'
| where Application == 'app.lab.local'
| project TimeGenerated, RequestURL, AccountObjectId
// SSRF IMDS 22bd0c
```

## Sinal

Egress filtering logs; deny metadata IMDS; alertas para 169.254.169.254.

## Freio

Nem todo fetch é SSRF explorável. WAF pode mascarar.
Não escaneio toda a rede interna sem autorização explícita.

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Evidência

DNS/HTTP callback proof; (se autorizado) trecho de metadata redigido.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP SSRF
- PortSwigger SSRF
- AWS IMDSv2