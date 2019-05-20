# XSS até account takeover — hardening

Do PoC ao controle — XSS até account takeover.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- Se não validar **CSRF token theft**, a nota fica genérica.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

## Camadas

1) Bloqueio imediato
2) CSP reports; WAF XSS signatures; canary cookies.
3) HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
checklist ato-chain:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (dcec84) falha
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