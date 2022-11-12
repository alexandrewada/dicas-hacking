# polkit histórico

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

## PoC mínimo

```bash
# linux privesc lab
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco pkexec tag 491b1e
```

## Diferencial desta nota

- Detalhe que pago pra ver: **Patch status**.

polkit histórico: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Auditd execve; sudo logs; file integrity.

## Onde já errei

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

Escape de container precisa de host PID/FS. Namespace cosmético não é host compromise.

## Entrega

- blue: Auditd execve; sudo logs; file integrity.
- fix: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.
- proof: Vetor; id antes/depois; artefato removido.

## Refs

- GTFOBins
- HackTricks Linux PrivEsc