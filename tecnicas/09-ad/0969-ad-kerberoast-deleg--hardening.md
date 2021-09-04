# roast + delegation abuse — hardening

Do PoC ao controle — roast + delegation abuse.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Detalhe que pago pra ver: **Encadeamento**.
- Roast + delegation são findings separados: senha fraca vs delegação excessiva.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

1) Bloqueio imediato
2) Event 4769 anômalos; honeypot SPNs; AES-only policies.
3) gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```text
checklist deleg:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (942522) falha
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting