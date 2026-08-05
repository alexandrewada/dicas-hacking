---
id: "0998"
categoria: "10-windows"
familia: "win-privesc"
slug: "token-dup"
angulo: "hardening"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "hardening", "t1548"]
aliases: ["token duplication", "token-dup", "token-dup-hardening"]
---

# token duplication — hardening

Do PoC ao controle — token duplication.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante token duplication: trato separado da família `win-privesc`.

## Camadas

Controle que fecha: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Sinal que deveria existir: Sysmon process creation; service changes; sticky potato patterns.

## PoC mínimo

```text
antes: controle ausente para token-dup
depois: ownership check / deny default em TARGET
verificação: PoC 6fa9af retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [token duplication](0238-win-privesc-token-dup.md)
- [token duplication — lab](0618-win-privesc-token-dup--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)