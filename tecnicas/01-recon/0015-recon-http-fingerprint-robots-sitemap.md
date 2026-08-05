---
id: "0015"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "robots-sitemap"
angulo: "base"
mitre: "T1592"
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "base", "t1592"]
aliases: ["robots.txt e sitemap.xml", "robots-sitemap"]
---

# robots.txt e sitemap.xml

**A05 Security Misconfiguration** · `T1592 Gather Victim Host Information`

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## O que muda aqui

- **Frequentemente listam painéis e APIs internas.** Sem isso o playbook da família mente.

## Como testo

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## No lab ficou assim

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag a61359 (robots-sitemap)
```

## Campo

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

robots.txt e sitemap.xml: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Detectar scanners por User-Agent e ritmo de probes. Alertar exposição de versões em headers.

## Já me queimei

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

## Blue

- Detectar: Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.
- Fechar: Remover headers reveladores; uniformizar erros; WAF + hardening de banner.

## Evidência

Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

## Refs

- [MITRE ATT&CK T1592](https://attack.mitre.org/techniques/T1592/)
- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [robots.txt e sitemap.xml — detecção](0395-recon-http-fingerprint-robots-sitemap--detecao.md)
- [robots.txt e sitemap.xml — path](0775-recon-http-fingerprint-robots-sitemap--path.md)
- [endpoints ACME/challenge](0020-recon-http-fingerprint-acme-probe.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)