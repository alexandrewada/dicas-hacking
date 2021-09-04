# detecção de ausência de gMSA — hardening

Do PoC ao controle — detecção de ausência de gMSA.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- **Finding defensivo.** Sem isso o playbook da família mente.
- Conta de serviço com SPN e sem gMSA: higiene defensiva. Senha gerenciada > keepass de 8 chars.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Controle que fecha: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Sinal que deveria existir: Event 4769 anômalos; honeypot SPNs; AES-only policies.

## Exemplo

```text
antes: controle ausente para gmsa
depois: ownership check / deny default em TARGET
verificação: PoC 3cd6b6 retorna 403/blocked
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