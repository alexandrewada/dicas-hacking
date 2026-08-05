---
id: "0898"
categoria: "05-injection"
familia: "inj-cmd"
slug: "busybox"
angulo: "hardening"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "hardening", "t1059"]
aliases: ["ambientes embedded/busybox", "busybox", "busybox-hardening"]
---

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

- [MITRE ATT&CK T1059](https://attack.mitre.org/techniques/T1059/)
- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [ambientes embedded/busybox — lab](0518-inj-cmd-busybox--lab.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [git options injection](0136-inj-cmd-git-hook.md)