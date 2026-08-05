---
id: "0254"
categoria: "11-linux"
familia: "linux-privesc"
slug: "cron"
angulo: "base"
mitre: ""
owasp: ""
tags: ["11-linux", "linux-privesc", "base"]
aliases: ["cron/wildcard injection", "cron"]
---

# cron/wildcard injection

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Detalhe

- Variante cron/wildcard injection: trato separado da família `linux-privesc`.

## Execução

1. Linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## No lab ficou assim

```bash
# linux cron — enum mínimo lab
ls -la /etc/cron* /var/spool/cron 2>/dev/null | head
showmount -e nfs.lab.local 2>/dev/null
echo $LD_PRELOAD
# kernel exploit: SOMENTE lab clonado — tag d974f3
# prod: evidencia de versão + CVE sem crash
```

## OpSec

Kernel exploits são instáveis — prefira misconfigs. Exploit local com crash potencial fica no lab clonado.

## Cuidados

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Fechamento

| | |
|---|---|
| Detecção | Auditd execve; sudo logs; file integrity. |
| Remediação | Remove SUID desnecessário; sudo least privilege; patch; immutable configs. |
| Evidência | Vetor; id antes/depois; artefato removido. |

## Refs

- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [cron/wildcard injection — evidência](0634-linux-privesc-cron--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)