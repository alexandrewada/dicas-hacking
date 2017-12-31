# template → command

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Detalhe

- **Geradores de relatório** — muda ruído e o que entra no PDF.

## Execução

1. Mapeio parâmetros que tocam filesystem/rede/conversão (ping, convert, git).
2. Injetar separadores e substituição de comando de forma controlada.
3. Preferir callbacks OOB a loops destrutivos.
4. Confirmar usuário e contêinerização.
5. Remover artefatos.

## PoC mínimo

```http
POST /tools/ping HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"host":"127.0.0.1; id"}
# lab only — saída de id prova inj template tag 1eaf7d
```

## OpSec

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Cuidados

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Fechamento

| | |
|---|---|
| Detecção | EDR: child process de web server; sysmon 1 rare chains. |
| Remediação | Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists. |
| Evidência | Output de `id`/`whoami`; árvore de processo; limpeza. |

## Refs

- OWASP Command Injection
- WSTG-INPV-12