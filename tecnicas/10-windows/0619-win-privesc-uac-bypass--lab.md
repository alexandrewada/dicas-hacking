---
id: "0619"
categoria: "10-windows"
familia: "win-privesc"
slug: "uac-bypass"
angulo: "lab"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "lab", "t1548"]
aliases: ["UAC bypass (lab)", "uac-bypass", "uac-bypass-lab"]
---

# UAC bypass (lab) — lab

Sandbox throwaway — UAC bypass (lab) sem ruído de cliente.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Se não validar **Documento detecção**, a nota fica genérica.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

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
sc.exe qc SVC_uac-bypass
# writable + priv service = privesc path tag 993798
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [UAC bypass (lab)](0239-win-privesc-uac-bypass.md)
- [UAC bypass (lab) — hardening](0999-win-privesc-uac-bypass--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)