---
id: "0996"
categoria: "10-windows"
familia: "win-privesc"
slug: "sched-task"
angulo: "hardening"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "hardening", "t1548"]
aliases: ["scheduled task ACL", "sched-task", "sched-task-hardening"]
---

# scheduled task ACL — hardening

Do PoC ao controle — scheduled task ACL.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Camadas

Hotfix: quebra a exploração direta de scheduled task ACL.
Detectivo: Sysmon process creation; service changes; sticky potato patterns.
Estrutural: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.

## Exemplo

```text
antes: controle ausente para sched-task
depois: ownership check / deny default em TARGET
verificação: PoC ecd9f1 retorna 403/blocked
reteste USER_A vs USER_B
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
- [PayloadsAllTheThings — Methodology and Resources](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Methodology%20and%20Resources)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [HackTricks — Windows Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Relacionadas

- [scheduled task ACL](0236-win-privesc-sched-task.md)
- [scheduled task ACL — lab](0616-win-privesc-sched-task--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)