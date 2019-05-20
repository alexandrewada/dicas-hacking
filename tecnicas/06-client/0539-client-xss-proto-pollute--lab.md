# prototype pollution → XSS — lab

Lab só pra prototype pollution → XSS. Se não reproduz isolado, não confio no finding de prod.

## Contexto

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Variante

- **jQuery sinks etc.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Gadget até sink. Sem gadget: hardening de merge, severidade menor.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

1. Mapeio reflections e sinks DOM (innerHTML, location, postMessage).
2. Testo contextos (HTML, attr, JS, URL, CSS).
3. Avalio cookies HttpOnly e CSP.
4. Construir PoC de impacto (sessão de teste / ação).
5. Verifico mutação por sanitizers (DOMPurify misconfig).

## No lab ficou assim

```html
<!-- reflected/stored lab payload — sem persistir em prod -->
<img src=x onerror="fetch('https://oast.lab.local/3de64e')">
<!-- sink proto-pollute: sessão USER_A / cookie flags -->
```

## Pitfall

Não capture sessões de usuários reais. Evito defacement.

CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.

## Prova do lab

PoC HTML; cookie flags; impacto narrado.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02