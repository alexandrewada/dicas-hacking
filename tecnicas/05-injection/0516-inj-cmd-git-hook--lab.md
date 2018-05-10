# git options injection — lab

Lab só pra git options injection. Se não reproduz isolado, não confio no finding de prod.

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Variante

- Se não validar **Quando app roda git**, a nota fica genérica.

## Setup

VM/conta throwaway na versão parecida.
Snapshot antes.
Cleanup escrito antes de explorar.

## Fluxo

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
# lab only — saída de id prova inj git-hook tag 4180e3
```

## Pitfall

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Prova do lab

Output de `id`/`whoami`; árvore de processo; limpeza.

## Refs

- OWASP Command Injection
- WSTG-INPV-12