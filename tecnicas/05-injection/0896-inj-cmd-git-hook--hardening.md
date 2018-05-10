# git options injection — hardening

Do PoC ao controle — git options injection.

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- Se não validar **Quando app roda git**, a nota fica genérica.

## Camadas

Controle que fecha: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
Sinal que deveria existir: EDR: child process de web server; sysmon 1 rare chains.

## Exemplo

```text
antes: controle ausente para git-hook
depois: ownership check / deny default em TARGET
verificação: PoC 420e94 retorna 403/blocked
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