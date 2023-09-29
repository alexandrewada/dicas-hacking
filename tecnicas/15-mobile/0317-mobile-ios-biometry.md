# biometry bypass lab

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Detalhe

- Se não validar **Local auth only**, a nota fica genérica.

## Execução

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## PoC mínimo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/biometry?token=TOKEN_LAB_c93ff3'
# deep link / exported → token sink
```

## OpSec

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

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