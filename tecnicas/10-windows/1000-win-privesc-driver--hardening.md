---
id: "1000"
categoria: "10-windows"
familia: "win-privesc"
slug: "driver"
angulo: "hardening"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "hardening", "t1548"]
aliases: ["vulnerable driver (BYOVD)", "driver", "driver-hardening"]
---

# vulnerable driver (BYOVD) — hardening

Do PoC ao controle — vulnerable driver (BYOVD).

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Se não validar **Somente se ROE e lab**, a nota fica genérica.

## Camadas

1) Bloqueio imediato
2) Sysmon process creation; service changes; sticky potato patterns.
3) Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
checklist driver:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (e15f01) falha
```

## Armadilha

Cuidado com AV/EDR em produção — combine com exclusions acordadas.
Não desabilito defesas sem autorização.

## Antes/depois

Vetor; whoami /priv; prova SYSTEM; cleanup.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1053](https://attack.mitre.org/techniques/T1053/)
- [PayloadsAllTheThings — Windows PrivEsc](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)
- [vulnerable driver (BYOVD) — lab](0620-win-privesc-driver--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [Potato / SeImpersonate](0233-win-privesc-potato.md)