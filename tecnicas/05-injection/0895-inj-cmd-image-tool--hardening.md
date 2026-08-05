---
id: "0895"
categoria: "05-injection"
familia: "inj-cmd"
slug: "image-tool"
angulo: "hardening"
mitre: "T1059"
owasp: "WSTG-INPV-12"
tags: ["05-injection", "inj-cmd", "hardening", "t1059"]
aliases: ["exiftool/ffmpeg/ImageMagick", "image-tool", "image-tool-hardening"]
---

# exiftool/ffmpeg/ImageMagick — hardening

Do PoC ao controle — exiftool/ffmpeg/ImageMagick.

## Risco

Command injection ocorre quando input entra em shell sem escaping (`;|&`$()`).
Teste expert distingue injection real de argument injection (sem shell) e usa out-of-band
para casos cegos. Impacto típico: RCE sob o usuário do serviço web.

## Controles desta variante

- **CVEs + injection.** Sem isso o playbook da família mente.

## Camadas

Hotfix: quebra a exploração direta de exiftool/ffmpeg/ImageMagick.
Detectivo: EDR: child process de web server; sysmon 1 rare chains.
Estrutural: Evitar shell; APIs parametrizadas; seccomp; containers non-root; allowlists.

## Exemplo

```bash
# verificação pós-hardening image-tool
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/image-tool/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 8f557a
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

- [exiftool/ffmpeg/ImageMagick](0135-inj-cmd-image-tool.md)
- [exiftool/ffmpeg/ImageMagick — lab](0515-inj-cmd-image-tool--lab.md)
- [argument injection sem shell](0133-inj-cmd-arg-inject.md)
- [ambientes embedded/busybox](0138-inj-cmd-busybox.md)
- [sendmail/pipe](0137-inj-cmd-email-pipe.md)
- [bypass de denylist](0139-inj-cmd-filter-bypass.md)