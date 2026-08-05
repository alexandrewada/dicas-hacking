---
id: "0017"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "cache-headers"
angulo: "base"
mitre: "T1592"
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "base", "t1592"]
aliases: ["heurística via Cache-Control/ETag", "cache-headers"]
---

# heurística via Cache-Control/ETag

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Detalhe

- Detalhe que pago pra ver: **Comportamento de CDN vs origem**.

## Execução

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## PoC mínimo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag 0f0028 (cache-headers)
```

## OpSec

WAF pode randomizar headers. Não confie só em `Server:`.

## Cuidados

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

## Fechamento

| | |
|---|---|
| Detecção | Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers. |
| Remediação | Remover headers reveladores; uniformizar erros; WAF + hardening de banner. |
| Evidência | Request/response sanitizados; versão inferida; confiança (alta/média/baixa). |

## Refs

- [MITRE ATT&CK T1592](https://attack.mitre.org/techniques/T1592/)
- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [heurística via Cache-Control/ETag — detecção](0397-recon-http-fingerprint-cache-headers--detecao.md)
- [heurística via Cache-Control/ETag — path](0777-recon-http-fingerprint-cache-headers--path.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)
- [páginas de erro verbosas](0013-recon-http-fingerprint-error-page.md)