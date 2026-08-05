---
id: "0897"
categoria: "05-injection"
familia: "inj-cmd"
slug: "email-pipe"
angulo: "hardening"
mitre: ""
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "hardening"]
aliases: ["sendmail/pipe", "email-pipe", "email-pipe-hardening"]
---

# sendmail/pipe — hardening

Do PoC ao controle — sendmail/pipe.

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- Detalhe que pago pra ver: **Legado clássico**.

## Camadas

Controle que fecha: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
Sinal que deveria existir: EDR: child process de web server; sysmon 1 rare chains.

## PoC mínimo

```text
checklist email-pipe:
- [ ] controle preventivo ativo
- [ ] telemetria cobre o PoC
- [ ] reteste com mesma prova (b78e10) falha
```

## Armadilha

Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

## Antes/depois

Output de `id`/`whoami`; árvore de processo; limpeza.

Aceite de risco só por escrito, com prazo.

## Refs

- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [sendmail/pipe — lab](0517-inj-cmd-email-pipe--lab.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [git options injection](0136-inj-cmd-git-hook.md)