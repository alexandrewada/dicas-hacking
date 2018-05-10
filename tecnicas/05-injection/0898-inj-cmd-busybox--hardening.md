# ambientes embedded/busybox — hardening

Do PoC ao controle — ambientes embedded/busybox.

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- Detalhe que pago pra ver: **Shell limitado**.

## Camadas

Controle que fecha: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
Sinal que deveria existir: EDR: child process de web server; sysmon 1 rare chains.

## No lab ficou assim

```text
checklist busybox:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (411b20) falha
```

## Armadilha

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Antes/depois

Output de `id`/`whoami`; árvore de processo; limpeza.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP Command Injection
- WSTG-INPV-12