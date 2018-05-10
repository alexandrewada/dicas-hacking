# argument injection sem shell — lab

Sandbox throwaway — argument injection sem shell sem ruído de cliente.

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Variante

- **flags extras em binários.** Sem isso o playbook da família mente.

## Setup

Ativo mínimo. Duas identidades se for authz.
Restore point.

## Fluxo

1. Mapeio parâmetros que tocam filesystem/rede/conversão (ping, convert, git).
2. Injetar separadores e substituição de comando de forma controlada.
3. Preferir callbacks OOB a loops destrutivos.
4. Confirmar usuário e contêinerização.
5. Remover artefatos.

## No lab ficou assim

```http
POST /tools/ping HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"host":"127.0.0.1; id"}
# lab only — saída de id prova inj arg-inject tag ece611
```

## Pitfall

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Prova do lab

Output de `id`/`whoami`; árvore de processo; limpeza.

## Refs

- OWASP Command Injection
- WSTG-INPV-12