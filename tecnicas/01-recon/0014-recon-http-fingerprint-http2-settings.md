---
id: "0014"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "http2-settings"
angulo: "base"
mitre: "T1592"
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "base", "t1592"]
aliases: ["HTTP/2 SETTINGS fingerprint", "http2-settings"]
---

# HTTP/2 SETTINGS fingerprint

`T1592 Gather Victim Host Information`

## Por que importa

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Variante

- Detalhe que pago pra ver: **Útil contra stacks modernas atrás de proxy**.

## Passo a passo

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Sinal / query

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag a7c34b (http2-settings)
```

## Nota de operador

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Armadilha

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

Já abri High demais em HTTP/2 SETTINGS fingerprint por sintoma sem efeito. Cruzei com: Detectar scanners por User-Agent e ritmo de probes. Alertar exposição de versões em headers. Sem side-effect, baixo.

## Depois

Detecção — Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

Remediação — Remover headers reveladores; uniformizar erros; WAF + hardening de banner.

No PDF — Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

## Refs

- [MITRE ATT&CK T1592](https://attack.mitre.org/techniques/T1592/)
- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [HTTP/2 SETTINGS fingerprint — detecção](0394-recon-http-fingerprint-http2-settings--detecao.md)
- [HTTP/2 SETTINGS fingerprint — path](0774-recon-http-fingerprint-http2-settings--path.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)