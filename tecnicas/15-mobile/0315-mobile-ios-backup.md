# itunes backup secrets

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Detalhe

- Variante itunes backup secrets: trato separado da família `mobile-ios`.

## Execução

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/backup?token=TOKEN_LAB_50e593'
# deep link / exported → token sink
```

## OpSec

Não contorne DRM de terceiros fora do escopo do app do cliente. Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Cuidados

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Fechamento

| | |
|---|---|
| Detecção | MDM policies; ATS force; keychain audit. |
| Remediação | Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC. |
| Evidência | Artefato Keychain de teste; request API. |

## Refs

- OWASP MASTG iOS