---
id: "0252"
categoria: "11-linux"
familia: "linux-privesc"
slug: "sudo"
angulo: "base"
mitre: "T1548"
owasp: ""
tags: ["11-linux", "linux-privesc", "base", "t1548"]
aliases: ["sudoers misconfig", "sudo"]
---

# sudoers misconfig

**Local privesc** · `T1548 / T1611`

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## O que muda aqui

- Se não validar **NOPASSWD abuse**, a nota fica genérica.

## Como testo

1. linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## Sinal / query

```bash
# sudo -l em lab; sem NOPASSWD abuse em prod sem ROE
sudo -l
# seguro: documentar comando permitido
# lab only: sudo vim -c ':!id'  # se NOPASSWD vim
# tag 51a68c (sudo)
```

## Campo

SUID/capabilities/docker.sock/sudo -l antes de kernel exploit barulhento.

Já abri High demais em sudoers misconfig por sintoma sem efeito. Cruzei com: Auditd execve; sudo logs; file integrity. Sem side-effect, baixo.

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

- [sudoers misconfig — evidência](0632-linux-privesc-sudo--evidencia.md)
- [SUID / GTFOBins](0251-linux-privesc-suid.md)
- [Abuso do grupo docker / sock](0256-linux-privesc-docker.md)
- [capabilities (cap_setuid)](0253-linux-privesc-caps.md)