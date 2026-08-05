---
id: "0257"
categoria: "11-linux"
familia: "linux-privesc"
slug: "ld-preload"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["LD_PRELOAD / hijack", "ld-preload"]
---

# LD_PRELOAD / hijack

**Local privesc** · `T1548 / T1611`

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

**Variante:** Variante LD_PRELOAD / hijack: trato separado da família `linux-privesc`.

**Método**

1. linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## Sinal / query

```bash
# linux ld-preload — enum mínimo lab
ls -la /etc/cron* /var/spool/cron 2>/dev/null | head
showmount -e nfs.lab.local 2>/dev/null
echo $LD_PRELOAD
# kernel exploit: SOMENTE lab clonado — tag 7d01ba
# prod: evidencia de versão + CVE sem crash
```

**Freio:** Kernel exploits são instáveis — prefira misconfigs.

Antes de Critical em LD_PRELOAD / hijack, confiro se a telemetria que eu cobraria reagiria — Auditd execve; sudo logs; file integrity.

Detecto via: Auditd execve; sudo logs; file integrity.

Corrijo com: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

Levo no report: Vetor; id antes/depois; artefato removido.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [LD_PRELOAD / hijack — evidência](0637-linux-privesc-ld-preload--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)