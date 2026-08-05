---
id: "0815"
categoria: "02-web"
familia: "web-upload"
slug: "imagemagick"
angulo: "path"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "path", "t1505"]
aliases: ["ImageMagick/Ghostscript sink", "imagemagick", "imagemagick-path"]
---

# ImageMagick/Ghostscript sink — path

ImageMagick/Ghostscript sink como pivô. Path curto > monte de finding isolado.

## Papel

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Por que pivota

- **SSRF/RCE históricos — verifique versão** — muda ruído e o que entra no PDF.

## Cadeia

1. Entrada (escopo)
2. Pivô: ImageMagick/Ghostscript sink
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## PoC mínimo

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----841f7e

------841f7e
Content-Disposition: form-data; name="file"; filename="probe_imagemagick.txt"
Content-Type: text/plain

lab-probe-841f7e
------841f7e--
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

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)
- [ImageMagick/Ghostscript sink — detecção](0435-web-upload-imagemagick--detecao.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [polyglot PDF/HTML](0053-web-upload-polyglot.md)