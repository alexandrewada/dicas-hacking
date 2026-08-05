---
id: "0615"
categoria: "10-windows"
familia: "win-privesc"
slug: "autologon"
angulo: "lab"
mitre: ""
owasp: ""
tags: ["10-windows", "win-privesc", "lab"]
aliases: ["autologon registry secrets", "autologon", "autologon-lab"]
---

# autologon registry secrets — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Variante

- Variante autologon registry secrets: trato separado da família `win-privesc`.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

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
sc.exe qc SVC_autologon
# writable + priv service = privesc path tag ab2318
```

## Pitfall

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

LOLBin: parent-child + linha de comando que o EDR deveria ter visto.

## Prova do lab

Vetor; whoami /priv; prova SYSTEM; cleanup.

## Refs

- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [autologon registry secrets](0235-win-privesc-autologon.md)
- [autologon registry secrets — hardening](0995-win-privesc-autologon--hardening.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)