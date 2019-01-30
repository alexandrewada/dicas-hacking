# stored XSS

**A03 Injection** · `T1189 Drive-by / T1059.007 JS`

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## O que muda aqui

- Se não validar **Perfil, markdown, suporte**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Como testo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## No lab ficou assim

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/fb67eb')">
<!-- sink stored: sessão USER_A / cookie flags -->
```

## Campo

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

Falso amigo em stored XSS: UI/log gritam, impacto não. Exijo CSP reports.

## Já me queimei

Não capture sessões de usuários reais. Evito defacement.

## Blue

- Detectar: CSP reports; WAF XSS signatures; canary cookies.
- Fechar: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Evidência

PoC HTML; cookie flags; impacto narrado.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02