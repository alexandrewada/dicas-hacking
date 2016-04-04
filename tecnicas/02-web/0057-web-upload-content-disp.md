# Content-Disposition injection

`T1505 Server Software Component`

## Por que importa

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Variante

- Se não validar **Header injection em downloads**, a nota fica genérica.

## Passo a passo

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----79e0bb

------79e0bb
Content-Disposition: form-data; name="file"; filename="probe_content-disp.txt"
Content-Type: text/plain

lab-probe-79e0bb
------79e0bb--
# sem webshell em prod; só lab
```

## Nota de operador

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Armadilha

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

Antes de Critical em Content-Disposition injection, confiro se a telemetria que eu cobraria reagiria — AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

## Depois

Detecção — AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

Remediação — Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.

No PDF — Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

## Refs

- WSTG-BUSL-08
- OWASP Unrestricted File Upload