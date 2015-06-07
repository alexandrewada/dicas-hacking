# paths /.well-known/

## Leitura rápida

Headers, ordem de cipher suites, HTTP/2 SETTINGS, cookies default e páginas de erro
permitem identificar stacks (IIS, nginx, Tomcat, Spring, Cloudflare) com baixa intrusão.
Em pentest externo, fingerprint preciso reduz ruído e evita payloads incompatíveis.

## Foco

- Se não validar **security.txt, change-password, oauth-authorization-server**, a nota fica genérica.

## Mãos na massa

1. Capturo response headers e cookies em request baseline.
2. Observar HTTP/2 e ALPN via TLS handshake autorizado.
3. Comparar com fingerprints conhecidos (wappalyzer logic / ja3s com cuidado).
4. Mapeio painéis admin por path heuristics **sem** força bruta agressiva.
5. Registrar versões expostas (Server, X-Powered-By) como finding informativo.

## Exemplo

```bash
# recon passivo autorizado
curl -sS 'https://crt.sh/?q=%25.lab.local&output=json' | jq '.[].name_value' | sort -u
# marcar dev-/staging- ; tag bee792 (well-known)
```

Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.

## Pitfall

WAF pode randomizar headers. Não confie só em `Server:`.
JA3/JA3S podem colidir; use como sinal, não prova.

## Detecção / remediação

Detectar scanners por User-Agent e ritmo de probes.
Alertar exposição de versões em headers.

→ Remover headers reveladores; uniformizar erros; WAF + hardening de banner.

## Prova

Request/response sanitizados; versão inferida; confiança (alta/média/baixa).

## Refs

- WSTG-INFO-02
- RFC 9110
- OWASP Secure Headers