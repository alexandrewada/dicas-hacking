# CSP bypass gadgets — hardening

Do PoC ao controle — CSP bypass gadgets.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **JSONP, CDNs antigos, nonce leak**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Hotfix: quebra a exploração direta de CSP bypass gadgets.
Detectivo: CSP reports; WAF XSS signatures; canary cookies.
Estrutural: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## Exemplo

```text
antes: controle ausente para csp-bypass
depois: ownership check / deny default em TARGET
verificação: PoC c9da58 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Não capture sessões de usuários reais. Evito defacement.

## Antes/depois

PoC HTML; cookie flags; impacto narrado.

Aceite de risco só por escrito, com prazo.

## Refs

- PortSwigger XSS
- OWASP XSS
- WSTG-INPV-01/02