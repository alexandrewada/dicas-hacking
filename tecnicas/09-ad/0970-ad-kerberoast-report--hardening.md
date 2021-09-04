# como reportar sem dump massivo — hardening

Do PoC ao controle — como reportar sem dump massivo.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Se não validar **Amostra mínima**, a nota fica genérica.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Hotfix: quebra a exploração direta de como reportar sem dump massivo.
Detectivo: Event 4769 anômalos; honeypot SPNs; AES-only policies.
Estrutural: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

## Exemplo

```bash
# verificação pós-hardening report
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/report/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 66c5a0
```

## Armadilha

Não pulverizo o KDC com milhares de requests. Evito contas prod críticas no crack público.

## Antes/depois

SPN list; hash crackado de conta lab/serviço fraco; path BloodHound.

Aceite de risco só por escrito, com prazo.

## Refs

- MITRE T1558
- SpecterOps Kerberoasting