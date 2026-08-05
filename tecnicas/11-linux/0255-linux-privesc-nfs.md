---
id: "0255"
categoria: "11-linux"
familia: "linux-privesc"
slug: "nfs"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["NFS no_root_squash", "nfs"]
---

# NFS no_root_squash

**Local privesc** · `T1548 / T1611`

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Como eu faço

1. Linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## No lab ficou assim

```bash
# linux nfs — enum mínimo lab
ls -la /etc/cron* /var/spool/cron 2>/dev/null | head
showmount -e nfs.lab.local 2>/dev/null
echo $LD_PRELOAD
# kernel exploit: SOMENTE lab clonado — tag 83698e
# prod: evidencia de versão + CVE sem crash
```

## Diferencial desta nota

- Variante NFS no_root_squash: trato separado da família `linux-privesc`.

Antes de Critical em NFS no_root_squash, confiro se a telemetria que eu cobraria reagiria — Auditd execve; sudo logs; file integrity.

## Onde já errei

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

Exploit local com crash potencial fica no lab clonado.

## Entrega

- blue: Auditd execve; sudo logs; file integrity.
- fix: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.
- proof: Vetor; id antes/depois; artefato removido.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [NFS no_root_squash — evidência](0635-linux-privesc-nfs--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)