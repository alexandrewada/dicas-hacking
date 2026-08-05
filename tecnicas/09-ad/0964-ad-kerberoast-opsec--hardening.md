---
id: "0964"
categoria: "09-ad"
familia: "ad-kerberoast"
slug: "opsec"
angulo: "hardening"
mitre: "T1558.003"
owasp: ""
tags: ["09-ad", "ad-kerberoast", "hardening", "t1558.003"]
aliases: ["opsec: stealthy roasting", "opsec", "opsec-hardening"]
---

# opsec: stealthy roasting — hardening

Do PoC ao controle — opsec: stealthy roasting.

## Risco

Kerberoasting solicita TGS de contas com SPN e cracking offline da cifra.
AS-REP roasting mira contas sem pre-auth. São técnicas core de AD com baixo ruído relativo
quando feitas com cuidado. No relatório enfatizo senhas fracas de serviço e tiering.

## Controles desta variante

- Detalhe que pago pra ver: **Taxa e targeting**.
- Priorizo serviço com SPN + password fraca. Dump de todo o domínio é amador e barulhento.

## Camadas

Hotfix: quebra a exploração direta de opsec: stealthy roasting.
Detectivo: Event 4769 anômalos; honeypot SPNs; AES-only policies.
Estrutural: gMSA/MSA; SPNs mínimos; senhas 25+; disable pre-auth só se necessário;
monitorar RC4.

## PoC mínimo

```text
antes: controle ausente para opsec
depois: ownership check / deny default em TARGET
verificação: PoC aa3d56 retorna 403/blocked
reteste USER_A vs USER_B
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

- [opsec: stealthy roasting](0204-ad-kerberoast-opsec.md)
- [opsec: stealthy roasting — lab](0584-ad-kerberoast-opsec--lab.md)
- [Kerberoasting (TGS RC4)](0201-ad-kerberoast-rc4.md)
- [AS-REP roasting](0203-ad-kerberoast-asrep.md)
- [path pós-roast](0205-ad-kerberoast-bloodhound.md)
- [detecção de ausência de gMSA](0206-ad-kerberoast-gmsa.md)