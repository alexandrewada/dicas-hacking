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

- OWASP Command Injection
- WSTG-INPV-12