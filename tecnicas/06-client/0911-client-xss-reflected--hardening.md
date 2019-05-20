# reflected XSS — hardening

Do PoC ao controle — reflected XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **Param → response sem encoding**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Controle que fecha: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Sinal que deveria existir: CSP reports; WAF XSS signatures; canary cookies.

## PoC mínimo

```bash
# verificação pós-hardening reflected
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/reflected/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag b23312
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