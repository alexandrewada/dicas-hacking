---
id: "0055"
categoria: "02-web"
familia: "web-upload"
slug: "imagemagick"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["ImageMagick/Ghostscript sink", "imagemagick"]
---

# ImageMagick/Ghostscript sink

**A04 Insecure Design / A03 Injection** · `T1505 Server Software Component`

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## O que muda aqui

- **SSRF/RCE históricos — verifique versão** — muda ruído e o que entra no PDF.

## Como testo

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## No lab ficou assim

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----5d90c4

------5d90c4
Content-Disposition: form-data; name="file"; filename="probe_imagemagick.txt"
Content-Type: text/plain

lab-probe-5d90c4
------5d90c4--
# sem webshell em prod; só lab
```

## Campo

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

ImageMagick/Ghostscript sink: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

## Já me queimei

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

## Blue

- Detectar: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.
- Fechar: Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.

## Evidência

Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [ImageMagick/Ghostscript sink — detecção](0435-web-upload-imagemagick--detecao.md)
- [ImageMagick/Ghostscript sink — path](0815-web-upload-imagemagick--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [polyglot PDF/HTML](0053-web-upload-polyglot.md)