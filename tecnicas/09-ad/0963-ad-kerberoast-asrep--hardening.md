# AS-REP roasting — hardening

Do PoC ao controle — AS-REP roasting.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- **Pre-auth disabled** — muda ruído e o que entra no PDF.
- DONT_REQ_PREAUTH = AS-REP roast sem SPN. Confirmo UAC no LDAP e limito amostra.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

1) Bloqueio imediato
2) Event 4769 anômalos; honeypot SPNs; AES-only policies.
3) gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## No lab ficou assim

```bash
# verificação pós-hardening asrep
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/asrep/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 9c9c74
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting