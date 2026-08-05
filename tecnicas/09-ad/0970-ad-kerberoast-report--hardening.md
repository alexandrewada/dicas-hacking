---
id: "0970"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "report"
angulo: "hardening"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "hardening", "t1558.003"]
aliases: ["como reportar sem dump massivo", "report", "report-hardening"]
---

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

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [como reportar sem dump massivo](0210-ad-kerberoast-report.md)
- [como reportar sem dump massivo — lab](0590-ad-kerberoast-report--lab.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)