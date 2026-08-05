---
id: "0235"
categoria: "10-windows"
familia: "win-privesc"
slug: "autologon"
angulo: "base"
mitre: ""
owasp: ""
tags: ["10-windows", "win-privesc", "base"]
aliases: ["autologon registry secrets", "autologon"]
---

# autologon registry secrets

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Detalhe

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Execução

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_autologon
# writable + priv service = privesc path tag ba573d
```

## OpSec

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Cuidados

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Fechamento

| | |
|---|---|
| Detecção | Sysmon process creation; service changes; sticky potato patterns. |
| Remediação | Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch. |
| Evidência | Vetor; whoami /priv; prova SYSTEM; cleanup. |

## Refs

- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [autologon registry secrets — lab](0615-win-privesc-autologon--lab.md)
- [autologon registry secrets — hardening](0995-win-privesc-autologon--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)