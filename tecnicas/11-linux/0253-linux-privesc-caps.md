---
id: "0253"
categoria: "11-linux"
familia: "linux-privesc"
slug: "caps"
angulo: "base"
mitre: ""
owasp: ""
tags: ["11-linux", "linux-privesc", "base"]
aliases: ["capabilities (cap_setuid)", "caps"]
---

# capabilities (cap_setuid)

## Leitura rápida

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Foco

- Variante capabilities (cap_setuid): trato separado da família `linux-privesc`.

## Mãos na massa

1. Linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## Sinal / query

```bash
getcap -r / 2>/dev/null | grep -E 'cap_setuid|cap_sys_admin' | tee caps_92454e.txt
# lab: explorar bin com cap_setuid+ep; prod: só inventário
# caps
```

Exploit local com crash potencial fica no lab clonado.

## Pitfall

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Detecção / remediação

Auditd execve; sudo logs; file integrity.

→ Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Prova

Vetor; id antes/depois; artefato removido.

## Refs

- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [capabilities (cap_setuid) — evidência](0633-linux-privesc-caps--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)