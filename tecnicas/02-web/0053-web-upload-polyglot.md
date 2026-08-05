---
id: "0053"
categoria: "02-web"
familia: "web-upload"
slug: "polyglot"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["polyglot PDF/HTML", "polyglot"]
---

# polyglot PDF/HTML

**A04 Insecure Design / A03 Injection** · `T1505 Server Software Component`

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

**Variante:** Se não validar **Útil contra validadores ingênuos**, a nota fica genérica.

**Método**

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## PoC mínimo

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----4a17ea

------4a17ea
Content-Disposition: form-data; name="file"; filename="probe_polyglot.txt"
Content-Type: text/plain

lab-probe-4a17ea
------4a17ea--
# sem webshell em prod; só lab
```

**Freio:** Não faço upload de malware real. Use webshells de lab benignas e remova ao final.

Já abri High demais em polyglot PDF/HTML por sintoma sem efeito. Cruzei com: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content. Sem side-effect, baixo.

Detecto via: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

Corrijo com: Storage fora de webroot; rename random; allowlist de tipos; re-encode de imagens;
desativar parsers perigosos; scanning.

Levo no report: Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [polyglot PDF/HTML — detecção](0433-web-upload-polyglot--detecao.md)
- [polyglot PDF/HTML — path](0813-web-upload-polyglot--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)