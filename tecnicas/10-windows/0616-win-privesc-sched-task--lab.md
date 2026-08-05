---
id: "0616"
categoria: "10-windows"
familia: "win-privesc"
slug: "sched-task"
angulo: "lab"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "lab", "t1548"]
aliases: ["scheduled task ACL", "sched-task", "sched-task-lab"]
---

# scheduled task ACL — lab

Lab só pra scheduled task ACL. Se não reproduz isolado, não confio no finding de prod.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

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
sc.exe qc SVC_sched-task
# writable + priv service = privesc path tag 67d7e4
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [scheduled task ACL](0236-win-privesc-sched-task.md)
- [scheduled task ACL — hardening](0996-win-privesc-sched-task--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)