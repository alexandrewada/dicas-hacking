# ACL pública pós-upload

**A04 Insecure Design / A03 Injection** · `T1505 Server Software Component`

## Contexto

Uploads mal validados levam a RCE (web shells), XSS armazenado, SSRF via SVG/XML,
e overwrite de arquivos críticos. No teste, cobre content-type spoofing, double extensions,
polyglots, path traversal no filename e processamento assíncrono (ImageMagick, LibreOffice).

## O que muda aqui

- **Object público indevido.** Sem isso o playbook da família mente.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

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
Content-Type: multipart/form-data; boundary=----3a2990

------3a2990
Content-Disposition: form-data; name="file"; filename="probe_s3-acl.txt"
Content-Type: text/plain

lab-probe-3a2990
------3a2990--
# sem webshell em prod; só lab
```

## Campo

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

Já abri High demais em ACL pública pós-upload por sintoma sem efeito. Cruzei com: AV/sandbox em upload; alertas de content-type mismatch; CSP em user content. Sem side-effect, baixo.

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

- WSTG-BUSL-08
- OWASP Unrestricted File Upload