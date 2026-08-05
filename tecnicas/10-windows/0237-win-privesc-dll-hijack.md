---
id: "0237"
categoria: "10-windows"
familia: "win-privesc"
slug: "dll-hijack"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "base", "t1548"]
aliases: ["DLL hijacking", "dll-hijack"]
---

# DLL hijacking

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## O que muda aqui

- **Apps trusted.** Sem isso o playbook da família mente.

## Como testo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_dll-hijack
# writable + priv service = privesc path tag cf560c
```

## Campo

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

DLL hijacking: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Sysmon process creation; service changes; sticky potato patterns.

## Já me queimei

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Blue

- Detectar: Sysmon process creation; service changes; sticky potato patterns.
- Fechar: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

## Evidência

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [DLL hijacking — lab](0617-win-privesc-dll-hijack--lab.md)
- [DLL hijacking — hardening](0997-win-privesc-dll-hijack--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)