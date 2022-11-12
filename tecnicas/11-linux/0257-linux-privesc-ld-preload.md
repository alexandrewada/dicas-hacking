# LD_PRELOAD / hijack

**Local privesc** · `T1548 / T1611`

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

**Variante:** Variante LD_PRELOAD / hijack: trato separado da família `linux-privesc`.

**Método**

1. linpeas/manual: sudo -l, find suid, caps, timers.
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
# foco ld-preload tag 7d01ba
```

**Freio:** Kernel exploits são instáveis — prefira misconfigs.

Antes de Critical em LD_PRELOAD / hijack, confiro se a telemetria que eu cobraria reagiria — Auditd execve; sudo logs; file integrity.

Detecto via: Auditd execve; sudo logs; file integrity.

Corrijo com: Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

Levo no report: Vetor; id antes/depois; artefato removido.

Refs: GTFOBins, HackTricks Linux PrivEsc