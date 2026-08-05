---
id: "0256"
categoria: "11-linux"
familia: "linux-privesc"
slug: "docker"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["Abuso do grupo docker / sock", "docker"]
---

# Abuso do grupo docker / sock

**Local privesc** · `T1548 / T1611`

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que muda aqui

- **Container escape path** — muda ruído e o que entra no PDF.
- Leitura de host FS ou create privilegiado. Cosmético de namespace não fecha.

## Como testo

1. linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## Sinal / query

```bash
# docker.sock / privileged — lab namespace
ls -la /var/run/docker.sock
# seguro em prod: reportar permissão sem spawn
# lab only: docker run -v /:/mnt --rm alpine chroot /mnt id
# tag 529e80
```

## Campo

Exploit local com crash potencial fica no lab clonado.

Antes de Critical em docker.sock / group docker, confiro se a telemetria que eu cobraria reagiria — Auditd execve; sudo logs; file integrity.

## Já me queimei

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Blue

- Detectar: Auditd execve; sudo logs; file integrity.
- Fechar: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Evidência

Vetor; id antes/depois; artefato removido.

## Refs

- [MITRE ATT&CK T1548](https://attack.mitre.org/techniques/T1548/)
- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [GTFOBins](https://gtfobins.github.io/)
- [HackTricks — Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation)

## Relacionadas

- [Abuso do grupo docker / sock — evidência](0636-linux-privesc-docker--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [sudoers misconfig](0252-linux-privesc-sudo.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)
- [docker.sock no pod (path)](../14-k8s/0295-k8s-escape-docker-sock.md)