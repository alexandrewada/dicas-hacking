---
id: "0232"
categoria: "10-windows"
familia: "win-privesc"
slug: "service-acl"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "base", "t1548"]
aliases: ["service binary ACL fraca", "service-acl"]
---

# service binary ACL fraca

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## O que muda aqui

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

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
sc.exe qc SVC_service-acl
# writable + priv service = privesc path tag 55b7f5
```

## Campo

LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.

Já abri High demais em service binary ACL fraca por sintoma sem efeito. Cruzei com: Sysmon process creation; service changes; sticky potato patterns. Sem side-effect, baixo.

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
- [PayloadsAllTheThings — Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [service binary ACL fraca — lab](0612-win-privesc-service-acl--lab.md)
- [service binary ACL fraca — hardening](0992-win-privesc-service-acl--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)