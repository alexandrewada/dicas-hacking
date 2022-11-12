# kernel exploit (lab)

## Contexto

PrivEsc Linux: SUID/SGID, capabilities, sudoers, writable cron, wildcards, namespaces,
kernel exploits (último recurso), e containers escapáveis. Enumeração disciplinada supera
exploit-as-a-service.

## Detalhe

- **CVE específico** — muda ruído e o que entra no PDF.

## Execução

1. Linpeas/manual: sudo -l, find suid, caps, timers.
2. Verifico versões e GTFOBins.
3. Exploro writable service files e paths.
4. Provar root com PoC; limpar.
5. Separar misconfig de kernel exploit no relatório.

## Exemplo

```bash
# linux privesc lab
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco kernel tag 10153d
```

## OpSec

Kernel exploits são instáveis — prefira misconfigs.

## Cuidados

Kernel exploits são instáveis — prefira misconfigs.
Não teste dirtypipe-like em hosts críticos sem janela.

## Fechamento

| | |
|---|---|
| Detecção | Auditd execve; sudo logs; file integrity. |
| Remediação | Remove SUID desnecessário; sudo least privilege; patch; immutable configs. |
| Evidência | Vetor; id antes/depois; artefato removido. |

## Refs

- GTFOBins
- HackTricks Linux PrivEsc