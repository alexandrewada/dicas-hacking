---
id: "0238"
categoria: "10-windows"
familia: "win-privesc"
slug: "token-dup"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "base", "t1548"]
aliases: ["token duplication", "token-dup"]
---

# token duplication

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

**Variante:** Variante token duplication: trato separado da família `win-privesc`.

**Método**

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## Sinal / query

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_token-dup
# writable + priv service = privesc path tag bcb499
```

**Freio:** Cuidado com AV/EDR em produção — combine com exclusions acordadas.

token duplication: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Sysmon process creation; service changes; sticky potato patterns.

Detecto via: Sysmon process creation; service changes; sticky potato patterns.

Corrijo com: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

Levo no report: Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [token duplication — lab](0618-win-privesc-token-dup--lab.md)
- [token duplication — hardening](0998-win-privesc-token-dup--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)