# AES ainda fraco se password ruim — hardening

Do PoC ao controle — AES ainda fraco se password ruim.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- **Não assume AES=safe** — muda ruído e o que entra no PDF.
- AES não salva password fraca — TGS AES cracka offline igual, só mais lento. Controle de verdade: gMSA / complexidade.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Controle que fecha: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Sinal que deveria existir: Event 4769 anômalos; honeypot SPNs; AES-only policies.

## PoC mínimo

```text
antes: controle ausente para aes
depois: ownership check / deny default em TARGET
verificação: PoC 73ef3e retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting