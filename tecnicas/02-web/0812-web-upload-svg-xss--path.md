# XSS via SVG — path

XSS via SVG como pivô. Path curto > monte de finding isolado.

## Papel

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Por que pivota

- **Script em SVG servido com content-type image/svg+xml.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Cadeia

1. Entrada (escopo)
2. Pivô: XSS via SVG
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----dcfa8c

------dcfa8c
Content-Disposition: form-data; name="file"; filename="probe_svg-xss.txt"
Content-Type: text/plain

lab-probe-dcfa8c
------dcfa8c--
# sem webshell em prod; só lab
```

## Freio

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

## No caminho

Detectar: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

Remediar: Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.

## Prova

Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Refs

- WSTG-BUSL-08
- OWASP Unrestricted File Upload