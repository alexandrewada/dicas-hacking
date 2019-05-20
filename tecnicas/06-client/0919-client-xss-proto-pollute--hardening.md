# prototype pollution → XSS — hardening

Do PoC ao controle — prototype pollution → XSS.

## Risco

XSS moderno raramente é `alert(1)`: o valor está em roubo de sessão, bypass de CSRF,
abuso de WebMessages e chain com CSP bypass. DOM XSS exige data flow (source→sink) real.

## Controles desta variante

- **jQuery sinks etc.** Sem isso o playbook da família mente.
- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Gadget até sink. Sem gadget: hardening de merge, severidade menor.

## Camadas

Controle que fecha: HttpOnly+Secure+SameSite; CSP nonce/hash; sanitização server+client;
Trusted Types.
Sinal que deveria existir: CSP reports; WAF XSS signatures; canary cookies.

## No lab ficou assim

```text
checklist proto-pollute:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (e37a19) falha
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