# DOM XSS — hardening

Do PoC ao controle — DOM XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- **location.hash → sink.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Hotfix: quebra a exploração direta de DOM XSS.
Detectivo: CSP reports; WAF XSS signatures; canary cookies.
Estrutural: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## PoC mínimo

```text
antes: controle ausente para dom
depois: ownership check / deny default em TARGET
verificação: PoC b0c49e retorna 403/blocked
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