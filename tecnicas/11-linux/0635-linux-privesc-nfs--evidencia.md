---
id: "0635"
categoria: "11-linux"
familia: "linux-privesc"
slug: "nfs"
angulo: "evidencia"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "evidencia", "t1548"]
aliases: ["NFS no_root_squash", "nfs", "nfs-evidencia"]
---

# NFS no_root_squash — evidência

Pacote pra NFS no_root_squash sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- Variante NFS no_root_squash: trato separado da família `linux-privesc`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (nfs)
hash_prova: de1103
```

## Remediação junto

Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Se purple

Auditd execve; sudo logs; file integrity.

## Armadilha

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [NFS no_root_squash](0255-linux-privesc-nfs.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)