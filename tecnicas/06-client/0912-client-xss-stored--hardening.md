# stored XSS — hardening

Do PoC ao controle — stored XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **Perfil, markdown, suporte**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

## Camadas

Hotfix: quebra a exploração direta de stored XSS.
Detectivo: CSP reports; WAF XSS signatures; canary cookies.
Estrutural: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.

## PoC mínimo

```bash
# verificação pós-hardening stored
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/stored/obj_ec9937 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag ec9937
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