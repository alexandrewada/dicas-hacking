---
id: "0993"
categoria: "10-windows"
familia: "win-privesc"
slug: "potato"
angulo: "hardening"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "hardening", "t1548"]
aliases: ["Potato / SeImpersonate", "potato", "potato-hardening"]
---

# Potato / SeImpersonate — hardening

Do PoC ao controle — Potato / SeImpersonate.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante Potato family (SeImpersonate): trato separado da família `win-privesc`.

## Camadas

1) Bloqueio imediato
2) Sysmon process creation; service changes; sticky potato patterns.
3) Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## PoC mínimo

```text
antes: controle ausente para potato
depois: ownership check / deny default em TARGET
verificação: PoC 73b2ed retorna 403/blocked
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

- [Potato / SeImpersonate](0233-win-privesc-potato.md)
- [Potato / SeImpersonate — lab](0613-win-privesc-potato--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [LSASS dump (autorizado) (path)](0241-win-cred-lsass.md)
- [Direitos de DCSync (path)](../09-ad/0213-ad-dacl-dcsync.md)