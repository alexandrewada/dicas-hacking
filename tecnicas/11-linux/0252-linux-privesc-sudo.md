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
# linux privesc lab
find / -perm -4000 -type f 2>/dev/null | head
sudo -l
getcap -r / 2>/dev/null | head
# foco sudo tag 51a68c
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

- GTFOBins
- HackTricks Linux PrivEsc