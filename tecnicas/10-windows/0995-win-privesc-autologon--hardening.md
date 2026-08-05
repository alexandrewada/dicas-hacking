---
id: "0995"
categoria: "10-windows"
familia: "win-privesc"
slug: "autologon"
angulo: "hardening"
mitre: ""
owasp: ""
tags: ["10-windows", "win-privesc", "hardening"]
aliases: ["autologon registry secrets", "autologon", "autologon-hardening"]
---

# autologon registry secrets — hardening

Do PoC ao controle — autologon registry secrets.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Camadas

Controle que fecha: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Sinal que deveria existir: Sysmon process creation; service changes; sticky potato patterns.

## PoC mínimo

```text
checklist autologon:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (7bf02d) falha
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [autologon registry secrets](0235-win-privesc-autologon.md)
- [autologon registry secrets — lab](0615-win-privesc-autologon--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)