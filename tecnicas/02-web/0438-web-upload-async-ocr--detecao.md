# pipeline OCR/async — detecção

Purple em pipeline OCR/async: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Hipótese

- **Arquivo malicioso processado por worker privilegiado** — muda ruído e o que entra no PDF.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1505 Server Software Component`.

### PoC

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```text
upload_log: unexpected content-type OR path traversal filename
async-ocr 0f2555
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

- WSTG-BUSL-08
- OWASP Unrestricted File Upload