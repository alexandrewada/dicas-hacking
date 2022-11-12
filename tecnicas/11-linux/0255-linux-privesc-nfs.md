# NFS no_root_squash

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

## No lab ficou assim

```bash
# linux privesc lab
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco nfs tag 83698e
```

## Diferencial desta nota

- Variante NFS no_root_squash: trato separado da família `linux-privesc`.

Antes de Critical em NFS no_root_squash, confiro se a telemetria que eu cobraria reagiria — Auditd execve; sudo logs; file integrity.

## Onde já errei

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

Exploit local com crash potencial fica no lab clonado.

## Entrega

- blue: Auditd execve; sudo logs; file integrity.
- fix: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.
- proof: Vetor; id antes/depois; artefato removido.

## Refs

- GTFOBins
- HackTricks Linux PrivEsc