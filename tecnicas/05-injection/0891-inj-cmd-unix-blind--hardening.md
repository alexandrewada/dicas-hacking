---
id: "0891"
categoria: "05-injection"
familia: "inj-cmd"
slug: "unix-blind"
angulo: "hardening"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "hardening", "t1059"]
aliases: ["Command injection cega (OOB)", "unix-blind", "unix-blind-hardening"]
---

# Command injection cega (OOB) — hardening

Do PoC ao controle — Command injection cega (OOB).

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- **curl/nslookup para collaborator** — muda ruído e o que entra no PDF.

## Camadas

1) Bloqueio imediato
2) EDR: child process de web server; sysmon 1 rare chains.
3) Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```text
antes: controle ausente para unix-blind
depois: ownership check / deny default em TARGET
verificação: PoC 922ce0 retorna 403/blocked
reteste USER_A vs USER_B
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

- [Command injection cega (OOB)](0131-inj-cmd-unix-blind.md)
- [Command injection cega (OOB) — lab](0511-inj-cmd-unix-blind--lab.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [SUID / GTFOBins (path)](../11-linux/0251-linux-privesc-suid.md)
- [Token de ServiceAccount (path)](../14-k8s/0291-k8s-escape-sa-token.md)