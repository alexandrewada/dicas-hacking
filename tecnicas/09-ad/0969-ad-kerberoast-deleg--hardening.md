---
id: "0969"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "deleg"
angulo: "hardening"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "hardening", "t1558.003"]
aliases: ["roast + delegation abuse", "deleg", "deleg-hardening"]
---

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

- [MITRE ATT&CK T1558.003](https://attack.mitre.org/techniques/T1558/003/)
- [MITRE ATT&CK T1558.004](https://attack.mitre.org/techniques/T1558/004/)
- [MITRE ATT&CK T1558](https://attack.mitre.org/techniques/T1558/)
- [SpecterOps — Kerberoasting](https://posts.specterops.io/kerberoasting-revisited-d9c270baaf91)
- [SpecterOps — BloodHound](https://bloodhound.specterops.io/)

## Relacionadas

- [roast + delegation abuse](0209-ad-kerberoast-deleg.md)
- [roast + delegation abuse — lab](0589-ad-kerberoast-deleg--lab.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)