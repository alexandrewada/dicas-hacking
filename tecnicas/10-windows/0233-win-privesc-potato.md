---
id: "0233"
categoria: "10-windows"
familia: "win-privesc"
slug: "potato"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "base", "t1548"]
aliases: ["Potato / SeImpersonate", "potato"]
---

# Potato / SeImpersonate

**Local privesc** · `T1548 Abuse Elevation Control / T1053`

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## O que muda aqui

- Variante Potato family (SeImpersonate): trato separado da família `win-privesc`.

## Como testo

1. Enumero com winPEAS/SharpUp/manual (serviços, tasks, registry).
2. Valido writability e restart conditions.
3. Exploro tokens privilegiados se presentes.
4. Provar SYSTEM com payload benigno.
5. Limpar persistência de teste.

## No lab ficou assim

```powershell
# lab Windows — enum sem LSASS dump em prod
Get-Acl C:\ServicePath\svc.exe | Format-List
sc.exe qc SVC_potato
# writable + priv service = privesc path tag 090484
```

## Campo

DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.

Falso amigo em Potato family (SeImpersonate): UI/log gritam, impacto não. Exijo Sysmon process creation.

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

- [Potato / SeImpersonate — lab](0613-win-privesc-potato--lab.md)
- [Potato / SeImpersonate — hardening](0993-win-privesc-potato--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [LSASS dump (autorizado) (path)](0241-win-cred-lsass.md)
- [Direitos de DCSync (path)](../09-ad/0213-ad-dacl-dcsync.md)