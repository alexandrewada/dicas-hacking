---
id: "0060"
categoria: "02-web"
familia: "web-upload"
slug: "heic"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["formatos less-common (HEIC/TIFF)", "heic"]
---

# formatos less-common (HEIC/TIFF)

## Leitura rápida

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Foco

- Se não validar **Parsers menos endurecidos**, a nota fica genérica.

## Mãos na massa

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## PoC mínimo

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----987748

------987748
Content-Disposition: form-data; name="file"; filename="probe_heic.txt"
Content-Type: text/plain

lab-probe-987748
------987748--
# sem webshell em prod; só lab
```

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Pitfall

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

## Detecção / remediação

AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

→ Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.

## Prova

Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [formatos less-common (HEIC/TIFF) — detecção](0440-web-upload-heic--detecao.md)
- [formatos less-common (HEIC/TIFF) — path](0820-web-upload-heic--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)
- [polyglot PDF/HTML](0053-web-upload-polyglot.md)