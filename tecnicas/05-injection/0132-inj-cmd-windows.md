---
id: "0132"
categoria: "05-injection"
familia: "inj-cmd"
slug: "windows"
angulo: "base"
mitre: ""
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "base"]
aliases: ["Windows cmd/PowerShell", "windows"]
---

# Windows cmd/PowerShell

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Detalhe

- **Certutil/iwr em lab.** Sem isso o playbook da família mente.

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
# lab only — saída de id prova inj windows tag 0a4445
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

- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [Windows cmd/PowerShell — lab](0512-inj-cmd-windows--lab.md)
- [Windows cmd/PowerShell — hardening](0892-inj-cmd-windows--hardening.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)