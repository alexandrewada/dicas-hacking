# Web: recon → ATO

Objetivo: sair do recon autorizado e chegar a account takeover (sessão de vítima controlada / fluxo OAuth abusado) com evidência que sobrevive peer review — sem phishing fora do ROE e sem PII real no PDF.

**Pré-condições:** escopo web + auth claros; contas de teste (attacker/victim); XSS/IDOR/OAuth no ROE; sem dump de usuários reais; CSRF/XSS stored só com payload inerte ou lab.

[Índice](../indice/README.md) · [Trilhas](README.md)

## Cadeia

1. **Recon passivo** — superfície e vazamentos sem tocar o alvo além do permitido.
   - [0001 — DNS / crt.sh](../tecnicas/01-recon/0001-recon-passive-dns-crtsh.md) · [path](../tecnicas/01-recon/0761-recon-passive-dns-crtsh--path.md)
   - [0015 — robots / sitemap](../tecnicas/01-recon/0015-recon-http-fingerprint-robots-sitemap.md)
   - [0021 — GitHub dorks](../tecnicas/01-recon/0021-recon-osint-people-github-dorks.md)

2. **IDOR horizontal** — objeto de outro usuário (ID numérico → UUID / batch).
   - [0031 — IDOR numérico](../tecnicas/02-web/0031-web-idor-numeric.md) · [path](../tecnicas/02-web/0791-web-idor-numeric--path.md) · [detecção](../tecnicas/02-web/0411-web-idor-numeric--detecao.md)
   - [0039 — IDOR horizontal](../tecnicas/02-web/0039-web-idor-horizontal.md) · [path](../tecnicas/02-web/0799-web-idor-horizontal--path.md)
   - [0040 — IDOR vertical](../tecnicas/02-web/0040-web-idor-vertical.md) (se o papel escalar)

3. **XSS → cadeia ATO** — cookie/token de sessão ou ação privilegiada no browser da vítima de teste.
   - [0151 — XSS reflected](../tecnicas/06-client/0151-client-xss-reflected.md) · [lab](../tecnicas/06-client/0531-client-xss-reflected--lab.md)
   - [0152 — XSS stored](../tecnicas/06-client/0152-client-xss-stored.md)
   - [0160 — XSS ATO chain](../tecnicas/06-client/0160-client-xss-ato-chain.md) · [lab](../tecnicas/06-client/0540-client-xss-ato-chain--lab.md) · [hardening](../tecnicas/06-client/0920-client-xss-ato-chain--hardening.md)

4. **OAuth / OIDC** — redirect aberto, state, PKCE quebrado → código/token na mão do attacker.
   - [0111 — redirect URI](../tecnicas/04-auth/0111-auth-oauth-oidc-redirect.md) · [path](../tecnicas/04-auth/0871-auth-oauth-oidc-redirect--path.md)
   - [0112 — state](../tecnicas/04-auth/0112-auth-oauth-oidc-state.md) · [path](../tecnicas/04-auth/0872-auth-oauth-oidc-state--path.md)
   - [0113 — PKCE](../tecnicas/04-auth/0113-auth-oauth-oidc-pkce.md)

5. **Session upgrade / MFA skip** — sessão “quase autenticada” vira full session.
   - [0110 — MFA bypass session upgrade](../tecnicas/04-auth/0110-auth-mfa-bypass-session-upgrade.md) · [path](../tecnicas/04-auth/0870-auth-mfa-bypass-session-upgrade--path.md) · [detecção](../tecnicas/04-auth/0490-auth-mfa-bypass-session-upgrade--detecao.md)

## Freios OpSec / quando parar

- XSS stored em produção: payload inerte (`alert` com tag de engajamento) ou só lab; limpo depois.
- IDOR: só objetos de contas de teste; PII mascarada no relatório.
- OAuth: não roubo sessão de usuário real; uso vítima controlada / redirect em domínio autorizado.
- Paro se o ROE exclui client-side ou alteração de dados de outros tenants — documento o path sem executar.

## O que entra no relatório

- Mapa recon → endpoint vulnerável (URL/param, sem wordlist dump).
- Prova IDOR: request/response de dois users de teste, IDs mascarados.
- Cadeia ATO: screenshot/HAR da sessão da vítima de teste pós-XSS ou OAuth.
- Fix: authZ por objeto, HttpOnly/CSP, redirect allowlist, state+PKCE, MFA binding à sessão.
- Links para as notas da cadeia (peer review reproduz).

[Índice](../indice/README.md)
