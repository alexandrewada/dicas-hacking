---
id: "0519"
categoria: "05-injection"
familia: "inj-cmd"
slug: "filter-bypass"
angulo: "lab"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "lab", "t1059"]
aliases: ["bypass de denylist", "filter-bypass", "filter-bypass-lab"]
---

# bypass de denylist — lab

Critério: outro analista fecha sozinho com esta nota.

## Contexto

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Variante

- Se não validar **IFS, quoting, wildcards**, a nota fica genérica.

## Setup

Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.

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
# lab only — saída de id prova inj filter-bypass tag 5af90f
```

## Pitfall

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Prova do lab

Output de `id`/`whoami`; árvore de processo; limpeza.

## Refs

- [MITRE ATT&CK T1059](https://attack.mitre.org/techniques/T1059/)
- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [bypass de denylist — hardening](0899-inj-cmd-filter-bypass--hardening.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [git options injection](0136-inj-cmd-git-hook.md)