---
id: "0259"
categoria: "11-linux"
familia: "linux-privesc"
slug: "systemd"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["systemd unit writable", "systemd"]
---

# systemd unit writable

`T1548 / T1611`

## Por que importa

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Variante

- Variante systemd unit writable: trato separado da família `linux-privesc`.

## Passo a passo

1. Linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## PoC mínimo

```bash
# linux privesc lab — systemd
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco systemd tag 9191d6
# exploit com crash: só lab clonado
```

## Nota de operador

Exploit local com crash potencial fica no lab clonado.

## Armadilha

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

systemd unit writable: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Auditd execve; sudo logs; file integrity.

## Depois

Detecção — Auditd execve; sudo logs; file integrity.

Remediação — Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

No PDF — Vetor; id antes/depois; artefato removido.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [systemd unit writable — evidência](0639-linux-privesc-systemd--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)