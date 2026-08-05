---
id: "0894"
categoria: "05-injection"
familia: "inj-cmd"
slug: "template"
angulo: "hardening"
mitre: ""
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "hardening"]
aliases: ["template → command", "template", "template-hardening"]
---

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

- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [template → command](0134-inj-cmd-template.md)
- [template → command — lab](0514-inj-cmd-template--lab.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)