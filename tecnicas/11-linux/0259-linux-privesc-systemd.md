# systemd unit writable

`T1548 / T1611`

## Por que importa

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Variante

- Variante systemd unit writable: trato separado da família `linux-privesc`.

## Passo a passo

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
# foco systemd tag 9191d6
```

## Nota de operador

Exploit local com crash potencial fica no lab clonado.

## Armadilha

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

systemd unit writable: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Auditd execve; sudo logs; file integrity.

## Depois

Detecção — Auditd execve; sudo logs; file integrity.

Remediação — Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

No PDF — Vetor; id antes/depois; artefato removido.

## Refs

- GTFOBins
- HackTricks Linux PrivEsc