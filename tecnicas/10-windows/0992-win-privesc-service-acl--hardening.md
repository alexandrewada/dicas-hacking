---
id: "0992"
categoria: "10-windows"
familia: "win-privesc"
slug: "service-acl"
angulo: "hardening"
mitre: "T1548"
owasp: ""
tags: ["10-windows", "win-privesc", "hardening", "t1548"]
aliases: ["service binary ACL fraca", "service-acl", "service-acl-hardening"]
---

# service binary ACL fraca — hardening

Do PoC ao controle — service binary ACL fraca.

## Risco

PrivEsc Windows combina misconfigs clássicas (unquoted service path, weak service ACL,
AlwaysInstallElevated, autologon registry) com token privileges (SeImpersonate → potato family)
e autostart extensibility. Metodologia: enum → hipótese → PoC mínimo → hardering.

## Controles desta variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.

## Camadas

Controle que fecha: Least privilege services; remove SeImpersonate de app pools quando possível;
hardening LAPS; patch.
Sinal que deveria existir: Sysmon process creation; service changes; sticky potato patterns.

## PoC mínimo

```bash
# verificação pós-hardening service-acl
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/service-acl/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 3367d9
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

- [service binary ACL fraca](0232-win-privesc-service-acl.md)
- [service binary ACL fraca — lab](0612-win-privesc-service-acl--lab.md)
- [AlwaysInstallElevated](0234-win-privesc-alwaysinstall.md)
- [autologon registry secrets](0235-win-privesc-autologon.md)
- [DLL hijacking](0237-win-privesc-dll-hijack.md)
- [vulnerable driver (BYOVD)](0240-win-privesc-driver.md)