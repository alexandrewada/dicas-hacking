---
id: "0133"
categoria: "05-injection"
familia: "inj-cmd"
slug: "arg-inject"
angulo: "base"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "base", "t1059"]
aliases: ["argument injection sem shell", "arg-inject"]
---

# argument injection sem shell

**A03 Injection** · `T1059 Command and Scripting Interpreter`

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Como eu faço

1. Mapeio parâmetros que tocam filesystem/rede/conversão (ping, convert, git).
2. Injetar separadores e substituição de comando de forma controlada.
3. Preferir callbacks OOB a loops destrutivos.
4. Confirmar usuário e contêinerização.
5. Remover artefatos.

## Sinal / query

```http
POST /tools/ping HTTP/1.1
Host: app.lab.local
Content-Type: application/json

{"host":"127.0.0.1; id"}
# lab only — saída de id prova inj arg-inject tag e5cff1
```

## Diferencial desta nota

- **flags extras em binários.** Sem isso o playbook da família mente.

Já abri High demais em argument injection sem shell por sintoma sem efeito. Cruzei com: EDR: child process de web server; sysmon 1 rare chains. Sem side-effect, baixo.

## Onde já errei

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Entrega

- blue: EDR: child process de web server; sysmon 1 rare chains.
- fix: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
- proof: Output de `id`/`whoami`; árvore de processo; limpeza.

## Refs

- [MITRE ATT&CK T1059](https://attack.mitre.org/techniques/T1059/)
- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [argument injection sem shell — lab](0513-inj-cmd-arg-inject--lab.md)
- [argument injection sem shell — hardening](0893-inj-cmd-arg-inject--hardening.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [git options injection](0136-inj-cmd-git-hook.md)