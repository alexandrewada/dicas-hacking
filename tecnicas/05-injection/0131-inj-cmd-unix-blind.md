---
id: "0131"
categoria: "05-injection"
familia: "inj-cmd"
slug: "unix-blind"
angulo: "base"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "base", "t1059"]
aliases: ["Command injection cega (OOB)", "unix-blind"]
---

# Command injection cega (OOB)

**A03 Injection** · `T1059 Command and Scripting Interpreter`

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

**Variante:** **curl/nslookup para collaborator** — muda ruído e o que entra no PDF.

**Método**

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
# lab only — saída de id prova inj unix-blind tag e1a0ee
```

**Freio:** Evito `rm -rf` e forks bombs. Em Windows, cuidado com PowerShell encoding.

Falso amigo em Unix cego com OOB DNS/HTTP: UI/log gritam, impacto não. Exijo EDR: child process de web server.

Detecto via: EDR: child process de web server; sysmon 1 rare chains.

Corrijo com: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.

Levo no report: Output de `id`/`whoami`; árvore de processo; limpeza.

## Refs

- [MITRE ATT&CK T1059](https://attack.mitre.org/techniques/T1059/)
- [WSTG-INPV-12](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
- [OWASP OS Command Injection Defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
- [PortSwigger — OS command injection](https://portswigger.net/web-security/os-command-injection)

## Relacionadas

- [Command injection cega (OOB) — lab](0511-inj-cmd-unix-blind--lab.md)
- [Command injection cega (OOB) — hardening](0891-inj-cmd-unix-blind--hardening.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)
- [SUID / GTFOBins (path)](../11-linux/0251-linux-privesc-suid.md)
- [Token de ServiceAccount (path)](../14-k8s/0291-k8s-escape-sa-token.md)