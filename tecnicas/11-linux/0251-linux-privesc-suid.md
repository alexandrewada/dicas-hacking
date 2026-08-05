---
id: "0251"
categoria: "11-linux"
familia: "linux-privesc"
slug: "suid"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["SUID / GTFOBins", "suid"]
---

# SUID / GTFOBins

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

## Sinal / query

```bash
# lab — SUID GTFO; prod: só enum
find / -perm -4000 -type f 2>/dev/null | tee suid_d61b22.txt
# seguro em prod: listar + comparar baseline
# destrutivo só em lab: ./vuln_suid -c 'id'  # NÃO em prod
gtfobins hint: suid
```

## Diferencial desta nota

- Variante SUID binaries GTFOBins: trato separado da família `linux-privesc`.

Falso amigo em SUID binaries GTFOBins: UI/log gritam, impacto não. Exijo Auditd execve.

## Onde já errei

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

SUID/capabilities/docker.sock/sudo -l antes de kernel exploit barulhento.

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

- [SUID / GTFOBins — evidência](0631-linux-privesc-suid--evidencia.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)