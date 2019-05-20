# postMessage origin wildcard — hardening

Do PoC ao controle — postMessage origin wildcard.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- **ATO via iframe** — muda ruído e o que entra no PDF.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

1) Bloqueio imediato
2) CSP reports; WAF XSS signatures; canary cookies.
3) HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
antes: controle ausente para postmessage
depois: ownership check / deny default em TARGET
verificação: PoC 811d64 retorna 403/blocked
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