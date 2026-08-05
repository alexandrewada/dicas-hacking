---
id: "0994"
categoria: "10-windows"
familia: "win-privesc"
slug: "alwaysinstall"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["10-windows", "win-privesc", "hardening"]
aliases: ["AlwaysInstallElevated", "alwaysinstall", "alwaysinstall-hardening"]
---

# AlwaysInstallElevated — hardening

Do PoC ao controle — AlwaysInstallElevated.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante AlwaysInstallElevated: trato separado da família `win-privesc`.

## Camadas

Controle que fecha: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Sinal que deveria existir: Sysmon process creation; service changes; sticky potato patterns.

## Exemplo

```text
checklist alwaysinstall:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (dcaf85) falha
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- [PayloadsAllTheThings — Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [AlwaysInstallElevated — lab](0614-win-privesc-alwaysinstall--lab.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)