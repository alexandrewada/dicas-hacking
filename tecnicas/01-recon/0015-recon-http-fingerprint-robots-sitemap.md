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

- WSTG-INFO-02
- RFC 9110
- OWASP Secure Headers