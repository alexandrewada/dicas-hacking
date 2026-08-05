---
id: "0433"
categoria: "02-web"
familia: "web-upload"
slug: "polyglot"
angulo: "detecao"
mitre: "T1505"
owasp: "WSTG-BUSL-08"
tags: ["02-web", "web-upload", "detecao", "t1505"]
aliases: ["polyglot PDF/HTML", "polyglot", "polyglot-detecao"]
---

# polyglot PDF/HTML — detecção

Gap de detecção em `T1505 Server Software Component` / polyglot PDF/HTML. PoC mínimo, telemetria ligada.

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Hipótese

- Se não validar **Útil contra validadores ingênuos**, a nota fica genérica.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```text
upload_log: unexpected content-type OR path traversal filename
polyglot a269dc
```

## Sinal

AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

## Freio

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Evidência

Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1505](https://attack.mitre.org/techniques/T1505/)
- [WSTG-BUSL-08](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic_Testing/08-Test_Upload_of_Unexpected_File_Types)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
- [PortSwigger — File upload vulnerabilities](https://portswigger.net/web-security/file-upload)

## Relacionadas

- [polyglot PDF/HTML](0053-web-upload-polyglot.md)
- [polyglot PDF/HTML — path](0813-web-upload-polyglot--path.md)
- [pipeline OCR/async](0058-web-upload-async-ocr.md)
- [Content-Disposition injection](0057-web-upload-content-disp.md)
- [formatos less-common (HEIC/TIFF)](0060-web-upload-heic.md)
- [ImageMagick/Ghostscript sink](0055-web-upload-imagemagick.md)