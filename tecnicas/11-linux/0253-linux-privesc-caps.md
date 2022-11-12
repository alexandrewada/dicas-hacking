# capabilities (cap_setuid)

## Leitura rápida

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Foco

- Variante capabilities (cap_setuid): trato separado da família `linux-privesc`.

## Mãos na massa

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
# foco caps tag 92454e
```

Exploit local com crash potencial fica no lab clonado.

## Pitfall

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Detecção / remediação

Auditd execve; sudo logs; file integrity.

→ Remove SUID desnecessário; sudo least privilege; patch; immutable configs.

## Prova

Vetor; id antes/depois; artefato removido.

## Refs

- GTFOBins
- HackTricks Linux PrivEsc