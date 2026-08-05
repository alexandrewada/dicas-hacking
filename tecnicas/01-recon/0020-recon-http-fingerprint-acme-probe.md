---
id: "0020"
categoria: "01-recon"
familia: "recon-http-fingerprint"
slug: "acme-probe"
angulo: "base"
mitre: "T1592"
owasp: "WSTG-INFO-02"
tags: ["01-recon", "recon-http-fingerprint", "base", "t1592"]
aliases: ["endpoints ACME/challenge", "acme-probe"]
---

# endpoints ACME/challenge

**A05 Security Misconfiguration** · `T1592 Gather Victim Host Information`

## Contexto

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Como eu faço

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## PoC mínimo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag aca1c4 (acme-probe)
```

## Diferencial desta nota

- **Indicam automação de cert e possíveis hosts efêmeros.** Sem isso o playbook da família mente.

Falso amigo em endpoints ACME/challenge: UI/log gritam, impacto não. Exijo Detectar scanners por User-Agent e ritmo de probes. Alertar exposição de versões em headers.

## Onde já errei

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.

## Entrega

- blue: Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.
- fix: Remover headers reveladores; uniformizar erros; WAF + hardening de banner.
- proof: Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

## Refs

- [MITRE ATT&CK T1592](https://attack.mitre.org/techniques/T1592/)
- [WSTG-INFO-02](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/02-Fingerprint_Web_Server)
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/)
- [PortSwigger — HTTP information gathering](https://portswigger.net/web-security)

## Relacionadas

- [endpoints ACME/challenge — detecção](0400-recon-http-fingerprint-acme-probe--detecao.md)
- [endpoints ACME/challenge — path](0780-recon-http-fingerprint-acme-probe--path.md)
- [heurística via Cache-Control/ETag](0017-recon-http-fingerprint-cache-headers.md)
- [cookies default de framework](0012-recon-http-fingerprint-cookie-banner.md)
- [CSP como mapa de domínios](0019-recon-http-fingerprint-csp-leak.md)
- [páginas de erro verbosas](0013-recon-http-fingerprint-error-page.md)