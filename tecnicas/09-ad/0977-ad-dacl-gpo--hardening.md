---
id: "0977"
categoria: "09-ad"
familia: "ad-dacl"
slug: "gpo"
angulo: "hardening"
mitre: "T1003"
owasp: ""
tags: ["09-ad", "ad-dacl", "hardening", "t1003"]
aliases: ["GPO abuse (Write)", "gpo", "gpo-hardening"]
---

# GPO abuse (Write) — hardening

Do PoC ao controle — GPO abuse (Write).

## Risco

BloodHound popularizou edges: GenericAll, WriteDACL, ForceChangePassword, DCSync rights,
AddMember, etc. valida o caminho em lab controlado e prova com ação mínima
(reset de conta teste, add a grupo lab), não com destruição.

## Controles desta variante

- Detalhe que pago pra ver: **Logon script plant**.

## Camadas

Controle que fecha: AdminSDHolder higiene; least privilege; Privileged Access Workstations;
remover ACEs excessivos.
Sinal que deveria existir: Directory Services Changes auditing; BloodHound Enterprise-like monitoring.

## PoC mínimo

```text
antes: controle ausente para gpo
depois: ownership check / deny default em TARGET
verificação: PoC 46f4e2 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

DCSync em produção é sensível — alinhe com cliente.
Evito resetar senhas de usuários reais.

## Antes/depois

Edge BloodHound; PoC controlado; ACE dump.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1003](https://attack.mitre.org/techniques/T1003/)
- [MITRE ATT&CK T1484](https://attack.mitre.org/techniques/T1484/)
- [SpecterOps — BloodHound docs](https://bloodhound.specterops.io/)
- [MITRE ATT&CK](https://attack.mitre.org/)

## Relacionadas

- [GPO abuse (Write)](0217-ad-dacl-gpo.md)
- [GPO abuse (Write) — lab](0597-ad-dacl-gpo--lab.md)
- [GenericAll em usuário/grupo](0211-ad-dacl-genericall.md)
- [Direitos de DCSync](0213-ad-dacl-dcsync.md)
- [KeyCredentialLink / Shadow Credentials](0220-ad-dacl-shadowcred.md)
- [WriteSPN → targeted roast](0216-ad-dacl-writespn.md)