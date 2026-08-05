---
id: "0633"
categoria: "11-linux"
familia: "linux-privesc"
slug: "caps"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["11-linux", "linux-privesc", "evidencia"]
aliases: ["capabilities (cap_setuid)", "caps", "caps-evidencia"]
---

# capabilities (cap_setuid) — evidência

Pacote pra capabilities (cap_setuid) sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- Variante capabilities (cap_setuid): trato separado da família `linux-privesc`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (caps)
hash_prova: f47930
```

## Remediação junto

Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Se purple

Auditd execve; sudo logs; file integrity.

## Armadilha

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Refs

- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)