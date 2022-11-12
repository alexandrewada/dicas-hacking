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
# linux privesc lab
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco suid tag d61b22
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

- GTFOBins
- HackTricks Linux PrivEsc