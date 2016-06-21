# XSS via SVG — detecção

Se o SOC não vê XSS via SVG, o finding é de cobertura, não de ego ofensivo.

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## Hipótese

- **Script em SVG servido com content-type image/svg+xml.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Mapeio tipos aceitos e onde o arquivo fica servido.
2. Testo MIME spoof, magic bytes, extensões (.php.png, .aspx;$), null bytes legados.
3. Avalio SVG/HTML/XML para XSS/XXE.
4. Verifico se o path de storage permite traversal.
5. Se processamento server-side existir, testar CVEs conhecidos do pipeline (com autorização).

## Sinal / query

```text
upload_log: unexpected content-type OR path traversal filename
svg-xss f5019e
```

## Sinal

AV/sandbox em upload; alertas de content-type mismatch; CSP em user content.

## Freio

Não faço upload de malware real. Use webshells de lab benignas e remova ao final.
Buckets S3 públicos são finding mesmo sem RCE.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Evidência

Arquivo de prova, URL de acesso, impacto demonstrado, limpeza documentada.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- WSTG-BUSL-08
- OWASP Unrestricted File Upload