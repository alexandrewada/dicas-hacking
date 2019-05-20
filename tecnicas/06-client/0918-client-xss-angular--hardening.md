# template injection client (Angular/Vue) — hardening

Do PoC ao controle — template injection client (Angular/Vue).

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Detalhe que pago pra ver: **SSTI client-side**.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

1) Bloqueio imediato
2) CSP reports; WAF XSS signatures; canary cookies.
3) HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening angular
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/angular/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 261231
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