# Command injection cega (OOB) — hardening

Do PoC ao controle — Command injection cega (OOB).

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- **curl/nslookup para collaborator** — muda ruído e o que entra no PDF.

## Camadas

1) Bloqueio imediato
2) EDR: child process de web server; sysmon 1 rare chains.
3) Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
antes: controle ausente para unix-blind
depois: ownership check / deny default em TARGET
verificação: PoC 922ce0 retorna 403/blocked
reteste USER_A vs USER_B
```

## Armadilha

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Antes/depois

Output de `id`/`whoami`; árvore de processo; limpeza.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP Command Injection
- WSTG-INPV-12