---
id: "0058"
categoria: "02-web"
familia: "web-upload"
slug: "async-ocr"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["pipeline OCR/async", "async-ocr"]
---

# pipeline OCR/async

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Detalhe

- **Arquivo malicioso processado por worker privilegiado** — muda ruído e o que entra no PDF.

## Execução

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----329c09

------329c09
Content-Disposition: form-data; name="file"; filename="probe_async-ocr.txt"
Content-Type: text/plain

lab-probe-329c09
------329c09--
# sem webshell em prod; só lab
```

## OpSec

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.

## Cuidados

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

## Fechamento

| | |
|---|---|
| Detecção | AV/sandbox em upload; alertas de content-type mismatch; CSP em user content. |
| Remediação | Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning. |
| Evidência | Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada. |

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [pipeline OCR/async — detecção](0438-web-upload-async-ocr--detecao.md)
- [pipeline OCR/async — path](0818-web-upload-async-ocr--path.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)
- [polyglot PDF/HTML](0053-web-upload-polyglot.md)