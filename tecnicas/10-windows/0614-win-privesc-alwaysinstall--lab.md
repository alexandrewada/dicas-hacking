---
id: "0614"
categoria: "10-windows"
familia: "win-privesc"
slug: "alwaysinstall"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["10-windows", "win-privesc", "lab"]
aliases: ["AlwaysInstallElevated", "alwaysinstall", "alwaysinstall-lab"]
---

# AlwaysInstallElevated — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Variante AlwaysInstallElevated: trato separado da família `win-privesc`.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

## Fluxo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## PoC mínimo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_alwaysinstall
# writable + priv service = privesc path tag dda74d
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [AlwaysInstallElevated — hardening](0994-win-privesc-alwaysinstall--hardening.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)