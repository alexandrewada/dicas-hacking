---
id: "0611"
categoria: "10-windows"
familia: "win-privesc"
slug: "unquoted"
angulo: "lab"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "lab", "t1548"]
aliases: ["unquoted service path", "unquoted", "unquoted-lab"]
---

# unquoted service path — lab

Lab só pra unquoted service path. Se não reproduz isolado, não confio no finding de prod.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Variante unquoted service path: trato separado da família `win-privesc`.

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

## Exemplo

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_unquoted
# writable + priv service = privesc path tag 515ffc
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

- [unquoted service path](0231-win-privesc-unquoted.md)
- [unquoted service path — hardening](0991-win-privesc-unquoted--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)