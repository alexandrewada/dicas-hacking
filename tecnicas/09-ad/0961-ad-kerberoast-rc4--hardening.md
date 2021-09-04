# Kerberoasting (TGS RC4) — hardening

Do PoC ao controle — Kerberoasting (TGS RC4).

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Detalhe que pago pra ver: **Encryption type downgrade**.
- RC4 ainda passa onde a policy AES existe no papel. Comparo etype do TGS com msDS-SupportedEncryptionTypes antes de chamar de hardenizado.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Controle que fecha: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.
Sinal que deveria existir: Event 4769 anômalos; honeypot SPNs; AES-only policies.

## No lab ficou assim

```bash
# verificação pós-hardening rc4
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/rc4/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 064f28
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting