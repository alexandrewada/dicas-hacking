---
id: "0052"
categoria: "02-web"
familia: "web-upload"
slug: "svg-xss"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["XSS via SVG", "svg-xss"]
---

# XSS via SVG

**A04 Insecure Design / A03 Injection** · `T1505 Server Software Component`

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Como eu faço

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## PoC mínimo

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----92229b

------92229b
Content-Disposition: form-data; name="file"; filename="probe_svg-xss.txt"
Content-Type: text/plain

lab-probe-92229b
------92229b--
# sem webshell em prod; só lab
```

## Diferencial desta nota

- **Script em SVG servido com content-type image/svg+xml.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

XSS via SVG: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

## Onde já errei

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Entrega

- blue: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.
- fix: Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.
- proof: Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [XSS via SVG — detecção](0432-web-upload-svg-xss--detecao.md)
- [XSS via SVG — path](0812-web-upload-svg-xss--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)