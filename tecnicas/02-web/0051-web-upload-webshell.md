---
id: "0051"
categoria: "02-web"
familia: "web-upload"
slug: "webshell"
angulo: "base"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "base", "t1505"]
aliases: ["web shell via extensão", "webshell"]
---

# web shell via extensão

**A04 Insecure Design / A03 Injection** · `T1505 Server Software Component`

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

**Variante:** Detalhe que pago pra ver: **Prove RCE com `id`/`whoami` e remova artefato**.

**Método**

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Exemplo

```http
POST /upload HTTP/1.1
Host: app.lab.local
Content-Type: multipart/form-data; boundary=----948ce7

------948ce7
Content-Disposition: form-data; name="file"; filename="probe_webshell.txt"
Content-Type: text/plain

lab-probe-948ce7
------948ce7--
# sem webshell em prod; só lab
```

**Freio:** Não faço upload de malware real. Use webshells de lab benignas e remova ao final.

Já abri High demais em web shell via extensão por sintoma sem efeito. Cruzei com: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content. Sem side-effect, baixo.

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

- [web shell via extensão — detecção](0431-web-upload-webshell--detecao.md)
- [web shell via extensão — path](0811-web-upload-webshell--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)