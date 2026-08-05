---
id: "0636"
categoria: "11-linux"
familia: "linux-privesc"
slug: "docker"
angulo: "evidencia"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "evidencia", "t1548"]
aliases: ["Abuso do grupo docker / sock", "docker", "docker-evidencia"]
---

# Abuso do grupo docker / sock — evidência

Pacote pra Abuso do grupo docker / sock sobreviver peer review.

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que precisa aparecer

- **Container escape path** — muda ruído e o que entra no PDF.
- Leitura de host FS ou create privilegiado. Cosmético de namespace não fecha.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Vetor; id antes/depois; artefato removido.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: f879dd

{"id":"obj_f879dd","owner":"USER_A","note":"redacted-docker"}
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

- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)
- [docker.sock no pod (path)](../14-k8s/0295-k8s-escape-docker-sock.md)