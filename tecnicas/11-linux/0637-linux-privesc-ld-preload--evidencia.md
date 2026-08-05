---
id: "0637"
categoria: "11-linux"
familia: "linux-privesc"
slug: "ld-preload"
angulo: "evidencia"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "evidencia", "t1548"]
aliases: ["LD_PRELOAD / hijack", "ld-preload", "ld-preload-evidencia"]
---

# LD_PRELOAD / hijack — evidência

Pacote pra LD_PRELOAD / hijack sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- Variante LD_PRELOAD / hijack: trato separado da família `linux-privesc`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: dc4e2d

{"id":"obj_dc4e2d","owner":"USER_A","note":"redacted-ld-preload"}
# capturado como USER_B
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

- [LD_PRELOAD / hijack](0257-linux-privesc-ld-preload.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)