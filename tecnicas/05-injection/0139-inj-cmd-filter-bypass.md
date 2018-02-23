# bypass de denylist

**A03 Injection** · `T1059 Command and Scripting Interpreter`

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

**Variante:** Se não validar **IFS, quoting, wildcards**, a nota fica genérica.

**Método**

1. Mapeio parâmetros que tocam filesystem/rede/conversão (ping, convert, git).
2. Injetar separadores e substituição de comando de forma controlada.
3. Preferir callbacks OOB a loops destrutivos.
4. Confirmar usuário e contêinerização.
5. Remover artefatos.

## Exemplo

```http
POST /tools/ping HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"host":"127.0.0.1; id"}
# lab only — saída de id prova inj filter-bypass tag 2cf5a1
```

**Freio:** Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

bypass de denylist: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: EDR: child process de web server; sysmon 1 rare chains.

Detecto via: EDR: child process de web server; sysmon 1 rare chains.

Corrijo com: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.

Levo no report: Output de `id`/`whoami`; árvore de processo; limpeza.

Refs: OWASP Command Injection, WSTG-INPV-12