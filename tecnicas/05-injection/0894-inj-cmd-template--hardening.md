# template → command — hardening

Do PoC ao controle — template → command.

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- **Geradores de relatório** — muda ruído e o que entra no PDF.

## Camadas

Hotfix: quebra a exploração direta de template → command.
Detectivo: EDR: child process de web server; sysmon 1 rare chains.
Estrutural: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.

## PoC mínimo

```bash
# verificação pós-hardening template
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/template/obj_e87166 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag e87166
```

## Armadilha

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Antes/depois

Output de `id`/`whoami`; árvore de processo; limpeza.

Aceite de risco só por escrito, com prazo.

## Refs

- OWASP Command Injection
- WSTG-INPV-12